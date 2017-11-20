from channels import include, route
from study_hard.consumers import ws_connect, ws_receive, ws_disconnect


websocket_routing = [
    route('websocket.connect', ws_connect),
    route('websocket.receive', ws_receive),
    route('websocket.disconnect', ws_disconnect),
]

channel_routing = [
    include('study_hard.routing.websocket_routing', path='^/chat_room/'),
    include('service_main.routing.custom_routing),
]
