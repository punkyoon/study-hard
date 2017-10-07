from django.db import models
from django.contrib.auth.models import User
from service_main.models import Study


class Notice(models.Model):
    _id = models.AutoField(primary_key=True)
    study = models.ForeignKey(Study, on_delete=models.CASCADE)
    upload_time = models.DateTimeField(auto_now_add=True)
    contents = models.TextField()

    def __str__(self):
        return str(self.study.title)


class Attendance(models.Model):
    _id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    study = models.ForeignKey(Study, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    # status list: attend, late, absent
    status = models.CharField(max_length=10, default='absent')

    def __str__(self):
        return str(self.user.username)