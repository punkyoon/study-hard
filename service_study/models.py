import time
import json
import hashlib

from django.db import models
from django.contrib.auth.models import User

from channels import Group

from service_main.models import Study


def _generate_hash():
    # Generate 7 character long hash
    now = str(time.time()).encode('utf-8')
    hash = hashlib.sha1(now)
    return hash.hexdigest()[:7]


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


class Fine(models.Model):
    _id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    study = models.ForeignKey(Study, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    fine_pay = models.BooleanField(default=False)
    fine_rate = models.IntegerField(default=0)
    fine_reason = models.TextField()
    hash_value = models.CharField(
        max_length=8,
        default=_generate_hash,
        unique=True
    )

    def __str__(self):
        return str(self._id)


class Chat(models.Model):
    _id = models.AutoField(primary_key=True)
    study = models.ForeignKey(Study, on_delete=models.CASCADE)
    message_datetime = models.DateTimeField(auto_now_add=True)
    message = models.TextField()

    def __str__(self):
        return str(self._id)

    @property
    def websocket_group(self):
        return Group(str(self.study.url))

    def send_message(self):
        msg = {
            'chat': self.study.url,
            'message': self.message,
            'msg_datetime': str(self.message_datetime),
        }

        self.websocket_group.send({
            'text': json.dumps(msg)
        })
