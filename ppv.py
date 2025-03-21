from database import get_user_info, get_random_message, get_suggested_ppv, record_ppv_sale
from onlyfans import send_message
import openai
from config import OPENAI_API_KEY

openai.api_key = OPENAI_API_KEY

def generate_ppv_message(username, video_title, video_url, video_price):
    """Genera un mensaje único de venta de PPV usando ChatGPT y la base de datos."""
    notable_info, last_messages = get_user_info(username)

    # Obtener un mensaje aleatorio de la base de datos
    base_message = get_random_message("PPV Promotions", username)

    # Prompt para ChatGPT
    prompt = f"""
    You are an OnlyFans model chatting with a subscriber. Your goal is to **sell a PPV video** while keeping the conversation fun and natural.

    🔹 **User Details:** {notable_info}
    🔹 **Recent Chat History:** {last_messages}
    🔹 **Video Title:** {video_title}
    🔹 **Video Price:** ${video_price}

    📩 **Example Sales Message:** "{base_message}"

    🎯 **Your Goal:**  
    - Write a UNIQUE and seductive PPV message.
    - Make the user feel like this offer is special for them.
    - Include the **video link**: {video_url}
    - Make sure the text is DIFFERENT from previous messages.

    🛑 **Rules:**  
    - Do NOT use generic phrases like "Just for you" (unless it fits naturally).
    - Be creative and flirty.
    - The message should sound human and not robotic.

    🔥 Now, generate the best sales message possible:
    """

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )

    return response["choices"][0]["message"]["content"]

def send_ppv_offer(driver, username):
    """Envía una oferta de PPV personalizada con un mensaje único."""
    video = get_suggested_ppv(username)  # Selecciona un video según gustos del usuario
    if video:
        video_title, video_url, video_price = video[1], video[2], video[4]

        # Generar un mensaje único para el PPV
        message = generate_ppv_message(username, video_title, video_url, video_price)

        # Enviar el mensaje
        send_message(driver, username, message)

        # Guardar venta en la base de datos
        record_ppv_sale(username, video_title, video_price)

        print(f"🎥 PPV offer sent to {username}")
