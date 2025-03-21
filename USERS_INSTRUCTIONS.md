# 👤 Instrucciones para Añadir Usuarios a la Base de Datos

Este documento te explica cómo introducir manualmente información importante de los suscriptores a la base de datos `onlyfans_bot.db`.

## 📌 Campos necesarios por usuario:

| Campo              | Descripción                                              |
|--------------------|----------------------------------------------------------|
| username           | El nombre de usuario (ID en OnlyFans)                   |
| name               | Nombre del usuario (opcional)                           |
| notable_info       | Gustos, si está casado, trabajo, edad, país, etc.       |
| last_30_messages   | Historial de mensajes recientes (se completa automáticamente) |
| purchased_videos   | Lista de títulos de videos comprados (se actualiza automáticamente) |
| total_spent        | Total gastado desde que es suscriptor (opcional)       |
| spent_last_month   | Lo que gastó en el último mes (opcional)               |

## 🛠 Cómo añadir un nuevo usuario:

1. Abre una terminal:
   ```bash
   sqlite3 onlyfans_bot.db

INSERT INTO users (username, name, notable_info, total_spent, spent_last_month)
VALUES ('john_doe', 'John', 'Le gusta el contenido de pies. Vive en Miami. Casado.', 120.50, 30.00);

SELECT * FROM users;

.exit
