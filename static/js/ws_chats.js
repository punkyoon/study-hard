var ws_chats = {
    handle_message: function (message) {
        message = message.trim();
        socket.send(JSON.stringify({
            'command': 'chat',
            'description': message,
            'room': room_path,
        }));
    },
    entityMap: {
        '<': '&lt;',
        '>': '&gt;',
        '"': '&quot;',
        "'": '&#39;',
        '&': '&amp;',
        '/': '&#x2F;',
        '`': '&#x60;',
        '=': '&#x3D',
    },
    escape_html: function (data) {
        return String(data).replace(/[&<>"'`=\/]/g, function (c) {
            return ws_chats.entityMap[c];
        });
    },
    new_chat: function (data) {
        var appended_msg = 0;

        appended_msg = $('\
            <div class="card">\
              <div class="card-header">\
                <p>' + ws_chats.escape_html(data.description) + '</p>\
              </div>\
            </div>\
        ');
        $('#chat-window').append(appended_msg);
    },
};
