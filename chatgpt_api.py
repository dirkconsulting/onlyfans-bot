import openai
from config import OPENAI_API_KEY
from database import get_user_info, get_random_message

openai.api_key = OPENAI_API_KEY

def generate_ai_response(username, new_message):
    """Genera respuestas de ChatGPT basadas en historial del usuario y datos personalizados."""
    notable_info, last_messages = get_user_info(username)

    # Obtener un mensaje de engagement aleatorio
    engagement_message = get_random_message("Engagement Messages", username)

    prompt = f"""
    You are an OnlyFans model having a conversation with a subscriber.

    🔹 **User Details:** {notable_info}
    🔹 **Recent Chat History:**  
    {last_messages}

    📩 **Latest Message from User:** "{new_message}"

    🎯 **Your Goal:**  
    - Keep the tone flirty and engaging.
    - Make the user feel special by referring to their interests.
    - Slowly build up excitement before introducing PPV content.
    - Use this engagement message as an example: "{engagement_message}"

    🛑 **Rules:**  
    - Do NOT use generic phrases or sound robotic.  
    - Make responses unique and natural.
    - The ultimate goal is to transition into a PPV sale.

    🔥 Now generate the best possible response:
    """

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )

    return response["choices"][0]["message"]["content"]
