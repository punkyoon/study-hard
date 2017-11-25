import json

from channels import Channel
from channels.auth import channel_session_user_from_http, channel_session_user

from study_hard.tool import _get_study


@channel_session_user_from_http
def ws_connect(message):
    message.reply_channel.send({'accept': True})
    message.channel_session['room'] = []


def ws_receive(message):
    payload = json.loads(message['text'])
    payload['reply_channel'] = message.content['reply_channel']
    Channel('room.receive').send(payload)


@channel_session_user
def ws_disconnect(message):
    for room_url in message.channel_session.get('room', set()):
        room = _get_study(room_url)
        if room is not None:
            room.websocket_group.discard(message.reply_channel)
