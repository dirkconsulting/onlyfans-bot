import sqlite3
from config import DB_PATH

def guardar_respuesta_exitosa(tipo, categoria_usuario, contenido_generado, resultado):
    """Guarda una respuesta generada que ha tenido buenos resultados."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO respuestas_exitosas (tipo, categoria_usuario, contenido_generado, resultado)
        VALUES (?, ?, ?, ?)
    """, (tipo, categoria_usuario, contenido_generado, resultado))

    conn.commit()
    conn.close()

def obtener_respuesta_exitosa(tipo, categoria_usuario):
    """Devuelve una respuesta exitosa aleatoria del mismo tipo y categoría de usuario."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
        SELECT contenido_generado FROM respuestas_exitosas
        WHERE tipo = ? AND categoria_usuario = ?
        ORDER BY RANDOM()
        LIMIT 1
    """, (tipo, categoria_usuario))

    result = cursor.fetchone()
    conn.close()

    return result[0] if result else None
