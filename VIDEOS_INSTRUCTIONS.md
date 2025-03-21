# 🎥 Instrucciones para Añadir Videos PPV a la Base de Datos

Aquí te mostramos cómo puedes subir videos manualmente a la base de datos `onlyfans_bot.db`, que luego serán recomendados por el bot.

## 🧾 Datos requeridos por video:

| Campo    | Descripción                              |
|----------|------------------------------------------|
| title    | Nombre del video (ej. "Mi ducha secreta")|
| url      | Enlace de OnlyFans o ubicación en Drive  |
| hashtags | Ej: #feet #shower #intimate               |
| price    | Precio del video en USD                   |

## 🛠 Cómo añadir un nuevo video:

1. Abre la base de datos:
   ```bash
   sqlite3 onlyfans_bot.db

INSERT INTO ppv_videos (title, url, hashtags, price)
VALUES ('Mi ducha secreta', 'https://onlyfans.com/file123', '#shower #wet #intimate', 14.99);

SELECT * FROM ppv_videos;

.exit
