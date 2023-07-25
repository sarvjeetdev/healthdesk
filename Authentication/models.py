from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator, MinValueValidator, validate_image_file_extension
import random
import os
from .models import *
from phone_field import PhoneField
from .managers import CustomUserManager


class User(AbstractUser):
    first_name = models.CharField(max_length=100, null=False, blank=False )
    phone = PhoneField(unique=True)
    last_name = models.CharField(max_length=100, null=False, blank=False )
    email = models.EmailField(max_length=256, null=True, blank=True, db_column="user_email")
    password = models.CharField(max_length=158, null=False, blank=False, db_column="user_password")
    username = None
    USERNAME_FIELD = "phone"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()


    def __str__(self):
        return str(self.phone)