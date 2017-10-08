from django.db import models
from django.contrib.auth.models import User
from accounts.models import Profile
from pokinator import Pokinator


def _generate_url():
    return Pokinator.generate()


class Study(models.Model):
    _id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=30)
    deposit = models.IntegerField(default=0)
    url = models.SlugField(unique=True, default=_generate_url)
    admin = models.ForeignKey(User, on_delete=models.CASCADE)
    is_available = models.BooleanField(default=True)
    description = models.TextField()

    def __str__(self):
        return str(self.title)


class StudyUser(models.Model):
    _id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    study = models.ForeignKey(Study, on_delete=models.CASCADE)
    deposit_pay = models.BooleanField(default=False)

    def __str__(self):
        return str(self.user.username)


class StudyRequest(models.Model):
    _id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    study = models.ForeignKey(Study, on_delete=models.CASCADE)
    approval = models.BooleanField(default=False)

    def __str__(self):
        return str(self.user)