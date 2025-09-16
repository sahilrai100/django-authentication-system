from django.shortcuts import render ,redirect ,get_object_or_404
from shoppingapp.forms import UserRegistrationForm,login_form,forgetPasswordForm,requestotp
from django.conf import settings

from django.core.mail import send_mail
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
import random
# Create your views here.

def random_numbers():
    return random.randint(999,10000)
value =random_numbers()


def home(request):
    
    return render(request,'home.html',{})

#!others
def forgetpassword(request):
    if request.method =='POST':
        forget_form=forgetPasswordForm(request.POST)
        if forget_form.is_valid():
                username=forget_form.cleaned_data['username']
                password=forget_form.cleaned_data.get('password')

                try:
                    user=User.objects.get(username=username)
                    user.set_password(password)
                    user.save()
                    return redirect('login')
                except User.DoesNotExist:
                    return redirect('forgetpassword')
    else:
        forget_form=forgetPasswordForm()

    return render(request,'forgetpassword.html',{'forget_form':forget_form})


@login_required(login_url='login')
def cart(request):
    return render(request,'cart.html')


def login_view(request):
    if request.user.is_authenticated:
        return redirect('home')


    if request.method =="POST":
        login_form_data=login_form(request.POST)
        if login_form_data.is_valid():  
            username=login_form_data.cleaned_data['username']
            password=login_form_data.cleaned_data['password']
            user=authenticate(request,username=username,password=password)
            if user:
                login(request,user)
                return redirect('home')
            else :
                return HttpResponse("credentials are not verified ")
    else:
        login_form_data=login_form()
    return render(request,'login.html',{'login_form_data':login_form_data})

def about(request):
    return render(request,'about.html')


def registration(request):
    user_form=UserRegistrationForm()
    if request.method =='POST':
        user_form=UserRegistrationForm(request.POST)
     
        if user_form.is_valid():
           
            email=user_form.cleaned_data['email']
            username=user_form.cleaned_data['username']
            site=site='http://127.0.0.1:8000/validation'

            user_form.save()
            subject = "Welcome to Zyanya 🎉"
            message = f"Hi {username},\n\nThank you for registering with us! \n your otp is {value} this otp is valid for 2 minutes\n click here --  to validate {site} "
            from_email = settings.EMAIL_HOST_USER
            recipient_list = [email]
            send_mail(subject, message, from_email, recipient_list ,fail_silently=True  )
            return redirect('validation')
    else:
        user_form=UserRegistrationForm()
     
    context={
        'user_form':user_form,
      
    }
    return render(request,'registration.html',context)

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def profile(request):
    return render(request,'profile.html',{})





def validation(request):
    if request.method =='POST':
        form=requestotp(request.POST)
        if form.is_valid():
            otp=form.cleaned_data.get('otp')
            print(otp)
            if otp == str(value): 
                print('success')
                return redirect('login')
            else:
                return HttpResponse("otp is not verified")
    else:
        form=requestotp()

    return render(request,'validation.html',{'form':form})



#! kids section
def kid_xander(request):
    return render(request,'kids_xander.html')

def kids_section_girl(request):
    return render(request,'kids_section_girl.html')

def kids_section_boy(request):
    return render(request,'kids_section_boy.html')







#! women's section


def women_section(request):
    return render(request,'women_section.html')

def sarees(request):
    return render(request,'sarees.html')

def salwar(request):
    return render(request,'salwar.html')

def kurti(request):
    return render(request,'kurti.html')

def lehanga(request):
    return render(request,'lehanga.html')

def women_jeans(request):
    return render(request,'women_jeans.html')

def women_inner(request):
    return render(request,'women_inner.html')


#! men's section 

def men_section(request):
    return render(request,'men_section.html')


def tshirt(request):
    return render(request,'tshirt.html')
def shirt(request):
    return render(request,'shirt.html')
def mens_jeans(request):
    return render(request,'mens_jeans.html')
def mens_inner(request):
    return render(request,'mens_inner.html')
def mens_suit(request):
    return render(request,'mens_suit.html')
def kurta(request):
    return render(request,'kurta.html')