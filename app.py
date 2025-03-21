from flask import Flask, render_template, request
import sqlite3
from config import DB_PATH

app = Flask(__name__)

# ========= PANEL DE RESPUESTAS ÉXITOSAS =========
def get_respuestas(tipo=None, resultado=None):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    query = """
    SELECT id, tipo, categoria_usuario, resultado, contenido_generado, fecha
    FROM respuestas_exitosas
    WHERE 1=1
    """
    filtros = []
    if tipo:
        query += " AND tipo = ?"
        filtros.append(tipo)
    if resultado:
        query += " AND resultado = ?"
        filtros.append(resultado)

    query += " ORDER BY fecha DESC"
    cursor.execute(query, filtros)
    rows = cursor.fetchall()
    conn.close()
    return rows

@app.route("/")
def index():
    tipo = request.args.get("tipo")
    resultado = request.args.get("resultado")
    respuestas = get_respuestas(tipo, resultado)
    return render_template("panel.html", respuestas=respuestas)

# ========= PANEL GENERAL DE ESTADÍSTICAS =========
@app.route("/dashboard")
def dashboard():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM users")
    user_count = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM ppv_videos")
    video_count = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM messages")
    message_count = cursor.fetchone()[0]

    cursor.execute("SELECT username, ultima_interaccion FROM users ORDER BY ultima_interaccion DESC LIMIT 10")
    recent_users = cursor.fetchall()

    conn.close()

    return render_template("dashboard.html", user_count=user_count, video_count=video_count,
                           message_count=message_count, recent_users=recent_users)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
