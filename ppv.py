from respuestas_exitosas import guardar_respuesta_exitosa, obtener_respuesta_exitosa
from database import get_user_info, get_random_message
from onlyfans import send_message
from config import OPENAI_API_KEY
import openai

openai.api_key = OPENAI_API_KEY

def generate_ppv_message(username, video_title, video_url, video_price, hashtags):
    """Genera un mensaje único de venta de PPV usando ChatGPT o reutiliza uno exitoso."""
    notable_info, last_messages = get_user_info(username)

    # 1. Intentar reutilizar una respuesta si ya hay una buena
    reused_response = obtener_respuesta_exitosa(tipo="ppv", categoria_usuario="nuevo")
    if reused_response:
        print(f"✅ Reutilizando respuesta PPV para {username}")
        return reused_response.replace("[VIDEO_URL]", video_url)

    # 2. Generar un nuevo mensaje con ChatGPT
    base_message = get_random_message("PPV Promotions")

    prompt = f"""
    You are a seductive OnlyFans model. You're chatting with a subscriber who is online now.

    🎥 You want to sell a **PPV video** with this info:
    - Title: {video_title}
    - Price: ${video_price}
    - Hashtags: {hashtags}

    🧠 Subscriber Info:
    - Notable Info: {notable_info}
    - Conversation History: {last_messages}

    🔥 Sales Message Inspiration: "{base_message}"

    🎯 Goal:
    - Write a UNIQUE, flirty and persuasive PPV message.
    - Make it feel personal and exclusive.
    - Include this video link: [VIDEO_URL]
    - Make sure it doesn’t sound like a copy-paste.

    Now create the best possible PPV message.
    """

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )

    ai_message = response["choices"][0]["message"]["content"].replace("[VIDEO_URL]", video_url)

    # 3. Guardar la respuesta para futuro reuso
    guardar_respuesta_exitosa(
        tipo="ppv",
        categoria_usuario="nuevo",
        contenido_generado=ai_message,
        resultado="venta_exitosa",
        video_id=None,  # Puedes actualizar con ID si quieres
        hashtags=hashtags
    )

    return ai_message

def send_ppv_offer(driver, username):
    """Envía una oferta de PPV personalizada con un mensaje único."""
    video = get_suggested_ppv(username)  # Selecciona un video según gustos del usuario
    if video:
        video_title, video_url, video_price, hashtags = video[1], video[2], video[3], video[5]

        # Generar un mensaje único para el PPV
        message = generate_ppv_message(username, video_title, video_url, video_price, hashtags)

        # Enviar el mensaje
        send_message(driver, username, message)

        # Guardar venta en la base de datos
        record_ppv_sale(username, video_title, video_price, hashtags)

        print(f"🎥 PPV offer sent to {username}")
