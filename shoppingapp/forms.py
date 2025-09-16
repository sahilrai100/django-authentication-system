from django import forms

from django.contrib.auth.models import User

from django.contrib.auth.forms import UserCreationForm

from captcha.fields import CaptchaField 

class UserRegistrationForm(UserCreationForm):
    email=forms.EmailField(required=True)
    captcha = CaptchaField()
    class Meta:
        model=User
        fields=['username','email','password1','password2','captcha']

    def clean_email(self):
        email=self.cleaned_data.get('email')
        if email and not email.endswith(('.com', '.in', '.org')):
            raise forms.ValidationError("email is not correct")
        if email:
          if  User.objects.filter(email=email).exists() :
              raise forms.ValidationError("email id already exist")
        
        return email
    

class login_form(forms.Form):
    username=forms.CharField(max_length=255)
    password=forms.CharField(widget=forms.PasswordInput)

    

class forgetPasswordForm(forms.Form):
    username=forms.CharField(max_length=150)
    password=forms.CharField(max_length=150,widget=forms.PasswordInput)
    confirm_password=forms.CharField(max_length=150,widget=forms.PasswordInput)
    
    def clean(self):
        cleaned_data = super().clean()
        
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password and confirm_password:
            
            if password != confirm_password:
                raise forms.ValidationError("password doest not match")
            
        return cleaned_data

class requestotp(forms.Form):
    otp=forms.CharField(max_length=4)

    def clean_otp(self):
        otp=self.cleaned_data.get('otp')
        if otp:
            if not otp.isnumeric():
                raise forms.ValidationError("otp must be only numbers")
            
        return otp






# class UserRegistrationForm(forms.ModelForm):
#     password=forms.CharField(max_length=20,widget=forms.PasswordInput)
#     class Meta:
#         model = User
#         fields = ['username', 'email', 'password']

#     def clean(self):
#         cleaned_data=super().clean()
#         username=cleaned_data.get('username')
#         email=cleaned_data.get('email')
#         password=cleaned_data.get('password')
        
#         if username and email and password:
#                 if len(username)<3:
#                     raise forms.ValidationError("username can not have less than 3 character's")
                
#                 if 58>ord(username[0]) >47:
#                     raise forms.ValidationError("username can not start with number")
                
#                 if email:
#                   if not email.endswith(('.com', '.in', '.org')):

#                     raise forms.ValidationError("Email must end with .com, .in, or .org")
                  
#                 if len(password)<8:
#                     raise forms.ValidationError("password should have at least 8 characters")

            

            
#         return cleaned_data

# class userprofileform(forms.ModelForm):
#     class Meta:
#         model=registration
#         fields = ['address', 'phone_number']

#     def clean(self):
#         cleaned_data=super().clean()
#         address=cleaned_data.get('address')
#         Phone_number=cleaned_data.get('phone_number')
#         if Phone_number:
#             if len(str(Phone_number)) != 10:
#                 raise forms.ValidationError("phone number must have at least 10 characters")
        

#         return cleaned_data



    



