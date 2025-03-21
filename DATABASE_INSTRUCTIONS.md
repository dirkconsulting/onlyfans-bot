# 📘 Manual para añadir información a la base de datos OnlyFans Bot

Este archivo te explica paso a paso cómo añadir manualmente datos a la base de datos del bot.

---

## 👤 1. Añadir información manual de usuarios

La tabla `users` almacena los datos personalizados de cada suscriptor.

### 🧩 Campos:
- `username`: Nombre de usuario de OnlyFans (único).
- `name`: Nombre del usuario (opcional).
- `notable_info`: Información personal (gustos, trabajo, edad...).
- `last_30_messages`: NO TOCAR (esto se actualiza automáticamente).
- `purchased_videos`: NO TOCAR (lo actualiza el bot).
- `total_spent`: Si lo sabes, puedes ponerlo.
- `spent_last_month`: Si lo sabes, puedes ponerlo.

### 💻 Cómo añadir un usuario manualmente:

1. Abre una terminal:
```bash
sqlite3 onlyfans_bot.db
```

2. Ejecuta esta consulta:
```sql
INSERT INTO users (username, name, notable_info, total_spent, spent_last_month) 
VALUES ('sexy_angel_23', 'Mike', 'Le gusta el yoga, vive en Miami, está casado', 35.0, 10.0);
```

3. Para salir, escribe:
```sql
.quit
```

---

## 🎥 2. Añadir videos PPV

La tabla `ppv_videos` contiene todos los videos que el bot puede ofrecer.

### 🧩 Campos:
- `title`: Título del video
- `url`: Enlace al archivo del video
- `hashtags`: Palabras clave (ej. boobs, lingerie, shower)
- `price`: Precio del video en dólares

### 💻 Cómo añadir un video PPV manualmente:

```bash
sqlite3 onlyfans_bot.db
```

```sql
INSERT INTO ppv_videos (title, url, hashtags, price) 
VALUES ('Hot Shower Scene', 'https://cdn.tuvideo.com/shower123.mp4', 'shower,wet,boobs', 25.0);
```

```sql
.quit
```

---

## 🧠 Recomendaciones:
- No pongas acentos ni caracteres especiales en los `hashtags`.
- Usa palabras en inglés siempre que sea posible para estandarizar.
- No repitas títulos de videos.

---

## 📍 Archivo de la base de datos
Ubicación: `onlyfans_bot.db`  
Puedes moverlo, copiarlo o hacer un backup con:
```bash
cp onlyfans_bot.db backup_onlyfans_bot.db
```

---
