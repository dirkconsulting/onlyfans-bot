# 📌 Gestión de Mensajes en la Base de Datos

Este documento explica cómo administrar los mensajes en la base de datos `onlyfans.db`. El bot usa estos mensajes para interactuar con los usuarios en diferentes momentos, evitando repeticiones y manteniendo la conversación natural.

---

## 🗃️ Categorías de Mensajes

La base de datos contiene **100 mensajes por categoría** en la tabla `messages`. Las categorías disponibles son:

- **Welcome Messages** → Mensajes de bienvenida al suscriptor.
- **Engagement Messages** → Mensajes para mantener la conversación activa.
- **Upsell Messages** → Mensajes que guían hacia una compra.
- **PPV Promotions** → Mensajes específicos para vender contenido PPV.

---

## 🔍 Ver Mensajes Existentes
Para listar todos los mensajes de una categoría en la base de datos, usa el siguiente comando en SQLite:

```sql
SELECT * FROM messages WHERE category='Engagement Messages';
```

Esto mostrará todos los mensajes guardados en esa categoría.

---

## ➕ Agregar Nuevos Mensajes
Si deseas agregar más mensajes manualmente, usa este comando en SQLite:

```sql
INSERT INTO messages (category, message) VALUES ('Welcome Messages', 'Hey love! I’m so happy you’re here 😘');
```

Si necesitas añadir **varios mensajes** desde un CSV, usa el script `upload_messages.py` con este comando:

```bash
python3 upload_messages.py
```

Asegúrate de que el archivo `onlyfans_bot_messages.csv` esté en la carpeta `/data/` y siga este formato:

```csv
category,message
Welcome Messages,"Hey there, sexy! 💋 Welcome to my private world."
Engagement Messages,"Tell me, what turns you on the most? 😏"
```

---

## ❌ Eliminar Mensajes
Si un mensaje se repite demasiado o no funciona bien, puedes eliminarlo con:

```sql
DELETE FROM messages WHERE message='Hey love! I’m so happy you’re here 😘';
```

Para eliminar todos los mensajes de una categoría:

```sql
DELETE FROM messages WHERE category='Upsell Messages';
```

⚠️ **Advertencia:** Esta acción es irreversible. Asegúrate de que realmente quieres eliminar los mensajes.

---

## ✏️ Actualizar Mensajes Existentes
Si necesitas modificar un mensaje sin eliminarlo, usa:

```sql
UPDATE messages SET message='Hey baby! Welcome to my secret world 💕' WHERE message='Hey love! I’m so happy you’re here 😘';
```

---

## 📌 Recomendaciones
- Mantén la variedad para evitar que los usuarios reciban mensajes repetidos.
- Actualiza los mensajes cada cierto tiempo para mantener el bot fresco.
- Usa mensajes personalizados con nombres y emojis para que parezcan más naturales.

---

## 🚀 Próximos Pasos
1. Verifica que `onlyfans_bot_messages.csv` contiene mensajes variados.
2. Usa `upload_messages.py` para importarlos.
3. Revisa la base de datos con `SELECT * FROM messages;` para asegurarte de que todo está cargado correctamente.

Ahora el bot tendrá siempre mensajes únicos y personalizados en cada conversación 🎉

