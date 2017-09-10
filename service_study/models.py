from django.db import models
from django.contrib.auth.models import User
from service_main.models import Study


class Notice(models.Model):
    _id = models.AutoField(primary_key=True)
    study = models.ForeignKey(Study, on_delete=models.CASCADE)
    upload_time = models.DateTimeField(auto_now_add=True)
    contents = models.TextField()


class Attendance(models.Model):
    _id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=True)
    study = models.ForeignKey(Study, on_delete=True)
    date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, default='absence')
