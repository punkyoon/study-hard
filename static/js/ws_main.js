var ws_scheme = window.location.protocol == 'https:' ? 'wss': 'ws';
var ws_path = ws_scheme + '://' + window.location.host + '/chat_room/';

//var socket = new WebSocket(ws_path);
var socket = new channels.WebSocketBridge();
var room_path = window.location.pathname.split('/')[1];

socket.connect(ws_path);
socket.listen(function (message) {
    console.log(message);
    if (message.chat) {
        var appended_msg = $(
            '<div class="card" style="margin-bottom: 10px;">\
              <div class="card-header">\
                <p>' + message.message + '</p>\
              </div>\
            </div>'
        );
        $('#chat-list').append(appended_msg);
    }
    else if (message.join) {
        console.log('join event');
    }
    else if( message.leave) {
        console.log('leave event');
    }
    else {
        console.log('cannot handle message');
    }
});

socket.socket.onopen = function () {
    console.log('connected');
    socket.send({
        'command': 'join',
        'room': room_path
    });
};

socket.socket.onclose = function () {
    socket.send({
        'command': 'leave',
        'room': room_path
    });
    console.log('closed');
};

socket.socket.onbeforeunload = function() {
    socket.send({
        'command': 'leave',
        'room': room_path
    });
};


/*
// Handle message
socket.onmessage = function (message) {
    // Decode JSON
    var data = JSON.parse(message.data);

    if (data.chat) {
        // New chat
        console.log(data.chat)
        console.log(data)
        ws_chats.new_chat(data);
    } else {
        //console.log('Cannot handle message');
    }
};
*/
