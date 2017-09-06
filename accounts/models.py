from django.db import models
from django.contrib.auth.models import User

from phonenumber_field.modelfields import PhoneNumberField


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    gender = models.CharField(max_length=8, default='Secret')
    phone = PhoneNumberField()
    institution = models.CharField(max_length=32, default='None')
