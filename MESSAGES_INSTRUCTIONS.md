# 📄 Instrucciones para Añadir Mensajes a la Base de Datos

Este archivo explica cómo puedes añadir **nuevos mensajes** para que el bot de OnlyFans tenga mayor variedad y **nunca repita frases**.

## 🗂 Formato del archivo CSV

El archivo debe llamarse `onlyfans_bot_messages.csv` y debe tener la siguiente estructura:

## ✅ Categorías válidas

Asegúrate de que la columna `category` contenga exactamente uno de estos valores:

- `Welcome Message`
- `Engagement Messages`
- `Upsell Messages`
- `PPV Promotions`

## 🧠 Consejos para redactar mensajes

- No repitas los mensajes existentes.
- Sé coqueta/o, sexy y natural.
- Mantén frases cortas y fáciles de entender.
- Incluye emojis cuando tenga sentido.

## 🚀 Cómo subir los nuevos mensajes

1. Abre el archivo `onlyfans_bot_messages.csv`.
2. Añade tus nuevos mensajes al final del archivo.
3. Guarda el archivo.
4. Ejecuta el siguiente comando:

   ```bash
   python3 upload_messages.py



