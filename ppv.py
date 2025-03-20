from database import get_user_info, get_random_message, check_purchase, save_purchase
from onlyfans import send_message
import openai
from config import OPENAI_API_KEY

openai.api_key = OPENAI_API_KEY

def generate_ppv_message(username, video_title, video_url, video_price):
    """Genera un mensaje único de venta de PPV usando ChatGPT basado en el usuario y su historial."""
    notable_info, last_messages = get_user_info(username)
    
    # Obtener un mensaje base de la categoría PPV Promotions
    base_message = get_random_message("PPV Promotions", username)

    # Prompt para ChatGPT
    prompt = f"""
    You are an OnlyFans model chatting with a fan. Your goal is to sell a **PPV video** in a seductive and engaging way.

    🔹 **User Details:** {notable_info}
    🔹 **Recent Messages:** {last_messages}
    🔹 **Video Title:** {video_title}
    🔹 **Video Price:** ${video_price}

    📩 **Example of a sales message:** "{base_message}"

    🎯 **Your Goal:**  
    - Write a UNIQUE, sexy and playful PPV message.
    - Make it feel natural and tailored to this user.
    - Include the **video link**: {video_url}
    - The message should be DIFFERENT from previous ones.
    
    🛑 **Rules:**  
    - Do NOT repeat generic phrases like "Just for you!" too often.
    - Make it sound flirty and real.
    - The message must feel personal.

    🔥 Generate the best message now:
    """

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )

    return response["choices"][0]["message"]["content"]

def get_suggested_ppv(username):
    """Obtiene un video PPV sugerido basado en el usuario y evita repetir contenido comprado."""
    from database import DB_PATH
    import sqlite3

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # Obtener videos NO comprados por el usuario
    cursor.execute("""
        SELECT * FROM ppv_videos WHERE id NOT IN (
            SELECT video_id FROM users WHERE username = ?
        ) ORDER BY RANDOM() LIMIT 1
    """, (username,))

    video = cursor.fetchone()
    conn.close()
    
    return video

def send_ppv_offer(driver, username):
    """Envía una oferta de PPV personalizada con un mensaje único."""
    video = get_suggested_ppv(username)  # Selecciona un video según gustos del usuario
    if video:
        video_id, video_title, video_url, hashtags, video_price = video

        # Verificar si el usuario ya ha comprado este PPV
        if not check_purchase(username, video_id):
            # Generar mensaje de venta personalizado
            message = generate_ppv_message(username, video_title, video_url, video_price)

            # Enviar el mensaje
            send_message(driver, username, message)

            # Registrar la compra en la base de datos
            save_purchase(username, video_id, video_price)

            print(f"✅ PPV offer sent to {username}: {video_title}")
        else:
            print(f"❌ User {username} already purchased this PPV. Skipping.")
