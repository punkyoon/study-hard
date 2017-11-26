import json

from channels.auth import channel_session_user

from study_hard.tool import _get_study
from service_study.models import Chat


@channel_session_user
def room_join(message):
    room = _get_study(message['room'])
    if room is None:
        print('Invalid study room')
    else:
        room.websocket_group.add(message.reply_channel)
        message.reply_channel.send({
            'text': json.dumps({
                'join': str(room.url),
                'title': room.title,
            }),
        })

        '''
        Group(message['room']).send({
            'text': json.dumps({
                'join': str(room.url),
                'title': room.title,
            })
        })
        '''


@channel_session_user
def room_leave(message):
    room = _get_study(message['room'])
    if room is None:
        print('Invalid study room')
    else:
        room.websocket_group.discard(message.reply_channel)
        message.reply_channel.send({
            'text': json.dumps({
                'leave': str(room.url),
            }),
        })


@channel_session_user
def room_chat(message):
    room = _get_study(message['room'])
    if room is None:
        print('Invalid study room')
    else:
        chat = Chat.objects.create(study=room, message=message['message'])
        chat.send_message()
