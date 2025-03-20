import openai
import random
from config import OPENAI_API_KEY
from database import get_user_info, get_random_message, user_recently_received_ppv

openai.api_key = OPENAI_API_KEY

def generate_ai_response(username, new_message):
    """Genera respuestas de ChatGPT basadas en historial y datos del usuario."""
    
    # Obtener información relevante del usuario
    notable_info, last_messages = get_user_info(username)

    # Obtener un mensaje de engagement aleatorio
    engagement_message = get_random_message("Engagement Messages")

    # Limitar el historial a los últimos 15 mensajes para evitar respuestas muy largas
    limited_history = "\n".join(last_messages.split("\n")[-15:])

    # Verificar si el usuario recibió un PPV recientemente para evitar spam
    ppv_status = "Sí" if user_recently_received_ppv(username) else "No"

    # Prompt mejorado para ChatGPT
    prompt = f"""
    You are an OnlyFans model chatting with a fan.
    
    🔹 **User Details:** {notable_info}
    🔹 **Conversation History (last 15 messages):**  
    {limited_history}

    📩 **Latest Message from User:** "{new_message}"

    🎯 **Goals:**  
    - Keep the conversation flirty and engaging.  
    - Make the fan feel special by using personal details from their profile.  
    - If the fan shows strong interest, smoothly lead into a PPV offer.  
    - If they have **recently** received a PPV offer: Avoid sending another too soon. (Recent PPV: {ppv_status})  
    - **Use this as an inspiration for your tone:** "{engagement_message}"  

    🛑 **Rules:**  
    - NEVER send a generic response.  
    - Your response must always be different from previous messages.  
    - Avoid repeating sales phrases.  
    - The final goal is to make the fan feel engaged and **maximize PPV sales.**

    🔥 Now generate three different responses so we can choose the best one:
    """

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        n=3  # Generar 3 respuestas y elegir una aleatoria
    )

    best_response = random.choice(response["choices"])["message"]["content"]

    return best_response
