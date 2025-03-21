📘 GUÍA PARA GESTIONAR LA BASE DE DATOS DE FORMA MANUAL

🧍‍♂️ Añadir o editar usuarios manualmente

Ejecuta el cliente de SQLite:

sqlite3 onlyfans.db

Y luego, para añadir un nuevo usuario:

INSERT INTO users (username, name, notable_info, last_30_messages, purchased_videos, total_spent, spent_last_month)
VALUES ("john_doe", "John", "Casado, le gusta el fitness y los pies", "", "", 0, 0);

Puedes repetir este comando con diferentes datos según el nuevo suscriptor.

Para ver todos los usuarios:

SELECT * FROM users;


⸻

🎥 Añadir un nuevo video PPV

Desde el mismo sqlite3 onlyfans.db:

INSERT INTO ppv_videos (title, url, hashtags, price)
VALUES ("Lencería roja sensual", "https://example.com/video1.mp4", "#lingerie #red #exclusive", 25);

Para ver todos los vídeos subidos:

SELECT * FROM ppv_videos;


⸻

📩 Consultar últimos mensajes de un usuario

SELECT last_30_messages FROM users WHERE username = "john_doe";


⸻

💰 Ver cuánto ha gastado un usuario

SELECT total_spent, spent_last_month FROM users WHERE username = "john_doe";


⸻

🧹 Limpiar tabla de usuarios (con precaución)

DELETE FROM users;


⸻

🔍 Buscar todos los usuarios que han comprado un video específico

SELECT * FROM ppv_videos WHERE title = "Lencería roja sensual";


