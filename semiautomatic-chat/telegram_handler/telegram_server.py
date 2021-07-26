from flask import Flask, request, jsonify
import requests

from config import TELEGRAM_INIT_WEBHOOK_URL, TELEGRAM_SEND_MESSAGE_URL
from socketio_client import SocketioClient

app = Flask(__name__)
requests.get(TELEGRAM_INIT_WEBHOOK_URL)

@app.route('/telegram', methods=['POST'])
def telegram():
    req = request.get_json()

    chat_id = req["message"]['chat']['id']
    incoming_message = req["message"]["text"]

    sc = SocketioClient(chat_id)
    outgoing_message = sc.message(incoming_message)

    res = requests.get(TELEGRAM_SEND_MESSAGE_URL.format(chat_id, outgoing_message))

    success = True if res.status_code == 200 else False
    return jsonify(success=success)

if __name__ == '__main__':
    app.run(port='8000', debug=True)