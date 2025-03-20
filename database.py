import sqlite3
import random
from config import DB_PATH
import openai

openai.api_key = "TU_OPENAI_API_KEY"

def init_db():
    """Inicializa la base de datos con todas las tablas necesarias."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # Tabla de Usuarios
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE,
        name TEXT,
        notable_info TEXT,  -- Intereses, trabajo, estado civil, etc.
        last_30_messages TEXT,
        purchased_videos TEXT,
        total_spent REAL DEFAULT 0,
        spent_last_month REAL DEFAULT 0,
        last_messages TEXT DEFAULT '' -- Para evitar repeticiones en mensajes
    )
    """)

    # Tabla de Mensajes
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS messages (
        category TEXT,
        message TEXT
    )
    """)

    # Tabla de Videos PPV
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS ppv_videos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT,
        url TEXT,
        hashtags TEXT,
        price REAL
    )
    """)

    conn.commit()
    conn.close()

# Ejecutar solo una vez para crear tablas
init_db()

def get_random_message(category, username):
    """Obtiene un mensaje aleatorio de la base de datos y evita repeticiones."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # Obtener mensajes de la categoría
    cursor.execute("SELECT message FROM messages WHERE category=?", (category,))
    messages = cursor.fetchall()
    
    # Obtener los últimos mensajes enviados al usuario
    cursor.execute("SELECT last_messages FROM users WHERE username=?", (username,))
    last_sent = cursor.fetchone()
    
    last_sent = last_sent[0].split("|") if last_sent and last_sent[0] else []
    
    # Filtrar mensajes que NO se hayan enviado antes
    available_messages = [msg[0] for msg in messages if msg[0] not in last_sent]

    # Si no hay mensajes nuevos, usamos ChatGPT para reformular uno
    if not available_messages:
        selected_message = random.choice([msg[0] for msg in messages])
        selected_message = generate_unique_message(selected_message)
    else:
        selected_message = random.choice(available_messages)

    # Actualizar historial de mensajes del usuario
    last_sent.append(selected_message)
    last_sent = last_sent[-20:]  # Solo guardamos los últimos 20 para optimización

    cursor.execute("UPDATE users SET last_messages=? WHERE username=?", ("|".join(last_sent), username))
    conn.commit()
    conn.close()

    return selected_message

def generate_unique_message(original_message):
    """Usa ChatGPT para modificar un mensaje y hacerlo único."""
    prompt = f"""
    Rewrite this OnlyFans message to make it **different but still engaging**:
    "{original_message}"

    📌 Rules:
    - Keep it flirty and playful
    - Do NOT repeat the exact same sentence
    - Add slight variations
    """

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )

    return response["choices"][0]["message"]["content"]

def get_user_info(username):
    """Obtiene la información relevante de un usuario (notable_info y últimos mensajes)."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("SELECT notable_info, last_30_messages FROM users WHERE username=?", (username,))
    user_data = cursor.fetchone()

    conn.close()

    return user_data if user_data else ("No data", "No recent messages")

def save_purchase(username, video_id, amount):
    """Registra la compra de un PPV en la base de datos."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # Guardar la compra del video
    cursor.execute("UPDATE users SET purchased_videos = COALESCE(purchased_videos, '') || ?, total_spent = total_spent + ?, spent_last_month = spent_last_month + ? WHERE username=?",
                   (f"{video_id}|", amount, amount, username))

    conn.commit()
    conn.close()

def check_purchase(username, video_id):
    """Verifica si el usuario ya compró un video."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("SELECT purchased_videos FROM users WHERE username=?", (username,))
    purchased = cursor.fetchone()

    conn.close()

    return video_id in purchased[0].split("|") if purchased and purchased[0] else False
