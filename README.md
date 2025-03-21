# 🤖 OnlyFans Bot - Automated Chat & PPV Sales

This bot automates **OnlyFans** conversations, engages with subscribers, and sells PPV content using **Selenium + ChatGPT**.

## 🌟 Features:
✅ **AI-Powered Chat:** ChatGPT generates personalized messages.  
✅ **PPV Sales Automation:** Detects online users and offers PPV videos.  
✅ **User Database:** Stores purchase history, interests, and last 30 messages.  
✅ **Message Randomization:** Avoids repetitive messages for higher engagement.  
✅ **Selenium Automation:** Sends messages and interacts with OnlyFans UI.  

---

## 📂 Project Structure

| File | Description |
|------|------------|
| `bot.py` | Main bot script. Detects online users, chats with them, and offers PPV. |
| `onlyfans.py` | Manages OnlyFans login, message sending, and user detection using Selenium. |
| `chatgpt_api.py` | Calls ChatGPT API to generate realistic responses for chats. |
| `ppv.py` | Automates PPV sales, ensuring unique messages and personalized offers. |
| `database.py` | Stores user data, message templates, and PPV content in SQLite. |
| `config.py` | Stores API keys and credentials (DO NOT SHARE THIS FILE). |

---

## 🚀 How to Use

### **1️⃣ Install Dependencies**
```bash
sudo apt update && sudo apt install python3 python3-venv git -y
cd ~/onlyfans_bot
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt


# 🤖 OnlyFans Bot Automation

Este proyecto automatiza completamente la gestión de una cuenta de OnlyFans, incluyendo interacciones con los suscriptores, ventas de contenido PPV personalizado, seguimiento de usuarios y respuestas generadas por inteligencia artificial.

## 🚀 Funcionalidades

✅ Detección de usuarios online en tiempo real  
✅ Envío de mensajes automáticos (bienvenida, interacción, promociones)  
✅ Conversaciones personalizadas usando ChatGPT (OpenAI API)  
✅ Sistema inteligente de ventas de contenido PPV  
✅ Evita contenido repetido para cada usuario  
✅ Base de datos con historial completo y perfiles personalizados  
✅ Panel web para visualizar respuestas exitosas y rendimiento  
✅ Soporte para proxies

---

## 📁 Estructura del Proyecto

onlyfans_bot/
├── bot.py                   → Script principal que ejecuta la automatización
├── chatgpt_api.py          → Comunicación con la API de OpenAI
├── config.py               → Configuración (API keys, rutas, etc.)
├── database.py             → Conexión y gestión de la base de datos
├── onlyfans.py             → Funciones específicas de Selenium para OnlyFans
├── ppv.py                  → Gestión y envío de contenido PPV
├── respuestas_exitosas.py  → Almacenamiento de respuestas que funcionaron
├── respuestas_tools.py     → Herramientas para analizar respuestas
├── templates/
│   └── index.html          → Panel web de visualización con Flask
├── app.py                  → Servidor web para ver estadísticas
├── onlyfans_bot.db         → Base de datos SQLite local
├── onlyfans_bot_messages.csv → Mensajes organizados por categoría
├── upload_messages.py      → Script para cargar mensajes iniciales
└── requirements.txt        → Dependencias del proyecto

---

## 🧠 Tecnologías utilizadas

- 🐍 Python 3.10+
- 💬 OpenAI (ChatGPT API)
- 🌐 Selenium
- 📦 SQLite3
- 🔐 Flask (para panel web)
- 🌍 Soporte para Proxies

---

## 🛠️ Cómo ejecutar el proyecto

1. **Clona el repositorio**

```bash
git clone https://github.com/dirkconsulting/onlyfans-bot.git
cd onlyfans_bot

2.	Activa el entorno virtual

source venv/bin/activate

3.	Instala las dependencias

pip install -r requirements.txt

4.	Lanza el bot

python bot.py

5. 	Inicia el panel web (opcional)

python app.py

📊 Acceso al panel

Abre tu navegador y entra en:

http://<tu_IP>:5000/

Aquí puedes ver:
	•	Respuestas exitosas
	•	Filtros por tipo de respuesta o resultado
	•	Análisis de rendimiento

⸻

✍️ Cómo añadir nuevos datos

Lee el archivo README_DB_HELP.md para saber:
	•	Cómo subir usuarios nuevos
	•	Cómo añadir contenido PPV
	•	Cómo actualizar información manualmente
