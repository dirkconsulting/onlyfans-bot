import time, random
from onlyfans import (
    login_onlyfans,
    get_online_users,
    get_subscribers,
    send_message,
    send_welcome_message,
    send_engagement_message,
    detect_new_online_users
)
from chatgpt_api import generate_ai_response
from database import (
    user_exists, create_user_record, update_user_last_interaction,
    save_conversation, get_user_info
)
from ppv import send_ppv_offer

# Inicia sesión en OnlyFans
driver = login_onlyfans()
prev_online_users = set()

print("🤖 Bot iniciado y listo para trabajar...")

def handle_new_subscribers():
    """Detecta nuevos suscriptores y les da la bienvenida."""
    subscribers = get_subscribers(driver)
    for username in subscribers:
        if not user_exists(username):
            create_user_record(username)
            send_welcome_message(driver, username)
            print(f"👋 Nuevo suscriptor: {username}")

def engage_online_users():
    """Engancha a los usuarios online con conversación personalizada y PPV."""
    global prev_online_users

    new_users = detect_new_online_users(driver, prev_online_users)
    print(f"🟢 Nuevos usuarios online: {new_users}")

    for username in new_users:
        notable_info, last_messages = get_user_info(username)

        # Generar respuesta de ChatGPT
        ai_response = generate_ai_response(username, last_messages)

        # Enviar respuesta
        send_message(driver, username, ai_response)

        # Guardar en base de datos
        update_user_last_interaction(username)
        save_conversation(username, ai_response, tipo="chat")

        # Con 60% de probabilidad se intenta vender un PPV
        if random.random() > 0.4:
            send_ppv_offer(driver, username)

    # Actualizamos la lista de usuarios conectados
    prev_online_users = set(get_online_users(driver))

# Bucle principal
while True:
    try:
        handle_new_subscribers()
        engage_online_users()
        time.sleep(300)  # Espera 5 minutos
    except Exception as e:
        print(f"❌ Error: {e}")
        time.sleep(60)
