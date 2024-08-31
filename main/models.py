from django.contrib.auth.models import AbstractUser
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.utils import timezone
import os

# Create your models here.

def user_directory_path(instance, filename):
    final_name = filename.split('.')
    ext = final_name[-1]
    name = final_name[0]
    return f"{instance.id}_{name}{ext}"

class Users(AbstractUser):
    GENDER_CHOICES = (
        ('F', 'Female'),
        ('M', 'Male'),
    )

    # username = models.CharField(max_length=150, unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    city = models.CharField(max_length=100, blank=True, null=True)
    phone = PhoneNumberField(blank=True, null=True)

    # password = models.CharField(max_length=50)

    def __str__(self):
        return self.first_name


class Products(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField(max_length=300)
    price = models.PositiveIntegerField(default=0)
    most_sale = models.BooleanField(default=False)
    image = models.ImageField(upload_to=user_directory_path, blank=True, null=True, default="images/product-1.png")

    def __str__(self):
        return self.title
