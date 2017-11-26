from channels import route
from service_study import consumers


custom_routing = [
    route('room.receive', consumers.room_join, command='^join$'),
    route('room.receive', consumers.room_leave, command='^leave$'),
    route('room.receive', consumers.room_chat, command='^chat$'),
]
