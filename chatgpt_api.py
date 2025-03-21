def generate_ai_response(username, new_message):
    """Genera respuestas de ChatGPT basadas en historial y datos del usuario."""
    notable_info, last_messages = get_user_info(username)

    # Intentar usar una respuesta existente si hay alguna útil
    reused_response = obtener_respuesta_exitosa(tipo="engagement", categoria_usuario="nuevo")
    if reused_response:
        print(f"✅ Reutilizando respuesta exitosa para {username}")
        return reused_response

    # Generar respuesta nueva con ChatGPT si no hay una reutilizable
    engagement_message = get_random_message("Engagement Messages")

    prompt = f"""
    You are an OnlyFans model chatting with a subscriber.

    🔹 **User Details:** {notable_info}
    🔹 **Conversation History:**  
    {last_messages}

    📩 **User's Latest Message:** "{new_message}"

    🎯 **Your Goal:**  
    - Be playful, seductive, and engaging  
    - Keep the conversation flowing  
    - Warm up the user to eventually sell PPV content  
    - Use this sample as inspiration: "{engagement_message}"

    🛑 **Rules:**  
    - No generic or robotic phrases  
    - Personalize the message as much as possible  
    - Your goal is to SELL eventually, but not aggressively

    ✨ Now generate the best possible reply:
    """

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )

    ai_reply = response["choices"][0]["message"]["content"]

    # Guardar la respuesta como exitosa para futuros usos
    guardar_respuesta_exitosa(
        tipo="engagement",
        categoria_usuario="nuevo",
        contenido_generado=ai_reply,
        resultado="alta_respuesta"
    )

    return ai_reply
