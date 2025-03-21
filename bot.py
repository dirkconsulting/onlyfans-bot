import time, random
from onlyfans import login_onlyfans, get_online_users, send_message
from chatgpt_api import generate_ai_response
from database import get_user_info, update_user_info, get_random_message, check_new_subscribers
from ppv import send_ppv_offer
from random import choice
from bot_logic import engage_online_users, handle_new_subscribers

# Iniciar sesión en OnlyFans
driver = login_onlyfans()

def handle_new_subscriber(username):
    """Envía un mensaje de bienvenida único a nuevos suscriptores."""
    welcome_message = get_random_message("Welcome Messages", username)
    send_message(driver, username, welcome_message)

def engage_online_users():
    """Identifica usuarios en línea, conversa con ellos y vende PPV de manera personalizada."""
    online_users = get_online_users(driver)

    for user in online_users:
        notable_info, last_messages = get_user_info(user)

        # Genera una respuesta de IA basada en el historial del usuario
        ai_response = generate_ai_response(user, last_messages)
        send_message(driver, user, ai_response)

        # Probabilidad de venta PPV (ajustable según la estrategia de ventas)
        if random.random() > 0.5:  # 50% de probabilidad de vender un PPV
            send_ppv_offer(driver, user)

        # Guardar la nueva interacción en la base de datos
        update_user_info(user, ai_response)

def get_random_message(category):
    messages = {
        "Welcome Messages": [
            "¡Hola! Gracias por suscribirte 😊",
            "¡Bienvenido! Estoy emocionada de tenerte aquí 😘"
        ]
    }
    return choice(messages.get(category, ["¡Hola!"]))

def send_welcome_message(driver, username):
    welcome_message = get_random_message("Welcome Messages")
    send_message(driver, username, welcome_message)

def handle_new_subscribers(driver):
    new_users = check_new_subscribers(driver)
    for user in new_users:
        send_welcome_message(driver, user)

# Loop de ejecución continua con intervalos para evitar bloqueos
while True:
    handle_new_subscribers(driver)
    engage_online_users(driver)
    time.sleep(300)  # Ejecutar cada 5 minutos

