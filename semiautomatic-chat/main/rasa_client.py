from threading import Event
import socketio
RASA_URL = 'http://localhost:5005'

# En este fichero se hace uso de un objeto de tipo Event para esperar
# que se resuelva la consulta al servidor de rasa.

class Aux(socketio.ClientNamespace):
    ev = Event()
    
    def on_bot_uttered(self, data):
        self.result = data
        self.ev.set()

class RasaClient:   
    def __init__(self):
        self.sio = socketio.Client()
        self.sio.connect(RASA_URL)

        self.temp = Aux()
        self.sio.register_namespace(self.temp)

    def message(self, msg):
        self.temp.ev.clear()
        self.sio.emit("user_uttered", {"session_id": self.sio.sid, "message": msg})
        self.temp.ev.wait()
        
        return self.temp.result['text']