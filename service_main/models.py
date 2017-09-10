from django.db import models
from django.contrib.auth.models import User


class Study(models.Model):
    _id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    deposit = models.IntegerField(default=0)
    url = models.URLField(unique=True)
    admin = models.ForeignKey(User, on_delete=models.CASCADE)


class StudyUser(models.Model):
    _id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    study = models.ForeignKey(Study, on_delete=models.CASCADE)
    fine = models.IntegerField(default=0)
    deposit_pay = models.BooleanField(default=False)


class StudyRequest(models.Model):
    _id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    study = models.ForeignKey(Study, on_delete=models.CASCADE)
    approval = models.BooleanField(default=False)
