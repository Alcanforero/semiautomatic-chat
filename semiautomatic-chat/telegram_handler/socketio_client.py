import socketio
SERVER_URL = 'http://127.0.0.1:8080'

class SocketioClient:
    def __init__(self, chat_id):
        self.sio = socketio.Client()
        self.sio.connect(SERVER_URL, headers={'X-ChatId': str(chat_id)})

    def message(self, msg):
        val = self.sio.call("message", msg)
        return val