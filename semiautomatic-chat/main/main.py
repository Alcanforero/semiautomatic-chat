import eventlet, socketio
from rasa_client import RasaClient

sio = socketio.Server()
app = socketio.WSGIApp(sio)

# Diccionario que almacena los pares sid-chatid para su posterior borrado.
user_ids = {}

# Cuando un mensaje se conecta por socket, se almacena su sid junto a su chatid.
@sio.event
def connect(sid, environ):
    user_ids[sid] = environ['HTTP_X_CHATID']

@sio.event
def message(sid, msg):
    rc = RasaClient()
    val = rc.message(msg)
    return val

# Cuando un socket se desconecta (por cierre de comunicación), se desconectan
# todos los asociados a ese mismo chat.
def disconnectChat(sid):
    id = user_ids[sid]
    for user_id, chat_id in user_ids.items():
        if chat_id == id:
            user_ids.pop(user_id)
            sio.disconnect(user_id)

if __name__ == '__main__':
    eventlet.wsgi.server(eventlet.listen(('127.0.0.1', 8080)), app)