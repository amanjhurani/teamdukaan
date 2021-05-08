from django.db import models

# Create your models here.

from django.contrib.auth.models import AbstractUser

class Account(AbstractUser):
    mobile_number = models.IntegerField(null=True,blank=True)
    is_verified = models.BooleanField(default=False)