from django.db import transaction
from django.core.cache import cache
from channels import Group
from channels.auth import channel_session_user


@channel_session_user
def room_join(message):
    pass


@channel_session_user
def room_leave(message):
    pass


@channel_session_user
def room_chat(message):
    pass
