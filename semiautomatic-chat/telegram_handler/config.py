# Dirección de la api para el chat del bot creado en Telegram a usar.
BASE_TELEGRAM_URL = 'https://api.telegram.org/bot1700499850:AAGAm6YRXvvDDnqFxDnnPsbRwvfLWgKTG74'
# Webhook desde el que se despliega el bot.
LOCAL_WEBHOOK_ENDPOINT = 'https://51fba41c5acc.ngrok.io/telegram'


# HTTP Request para establecer el webhook y conjugar el chat de telegram con el bot de python
TELEGRAM_INIT_WEBHOOK_URL = '{}/setWebhook?url={}'.format(BASE_TELEGRAM_URL, LOCAL_WEBHOOK_ENDPOINT)

# HTTP Request para el envío de mensajes al chat
TELEGRAM_SEND_MESSAGE_URL = BASE_TELEGRAM_URL + '/sendMessage?chat_id={}&text={}'