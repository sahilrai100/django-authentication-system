# from django.db import models
# from django.contrib.auth.models import User

# # Create your models here.

# class registration(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)

#     address=models.CharField(max_length=255,null=True,blank=True)
#     phone_number=models.PositiveIntegerField()
#     age=models.CharField(max_length=3)
#     def __str__(self):
#         return self.user.username

# from django.db import models
# from django.contrib.auth.models import User
# # from shoppingapp.models import Product  # assuming you have a Product model for sarees

# class Cart(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     product = models.ForeignKey(Product, on_delete=models.CASCADE)
#     quantity = models.PositiveIntegerField(default=1)

#     def __str__(self):
#         return f"{self.user.username} - {self.product.name}"

#     def total_price(self):
#         return self.quantity * self.product.price

        