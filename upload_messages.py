import sqlite3
import csv

# Database connection
db_file = "onlyfans_bot.db"
csv_file = "onlyfans_bot_messages.csv"

conn = sqlite3.connect(db_file)
cursor = conn.cursor()

# Ensure table exists
cursor.execute("""
CREATE TABLE IF NOT EXISTS messages (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    category TEXT,
    message TEXT
)
""")

with open(csv_file, "r", encoding="utf-8") as file:
    reader = csv.reader(file)
    headers = next(reader)  # Skip the header row

    for row in reader:
        if len(row) < 4:  # Ensure there are four columns
            continue
        
        categories = ["Welcome", "Engagement", "Upsell", "PPV"]  # Adjust category names if needed
        
        for i in range(4):  # Loop through each message type
            message = row[i].strip()  # Clean whitespace
            if message:  # Ensure it's not empty
                cursor.execute("INSERT INTO messages (category, message) VALUES (?, ?)", (categories[i], message))

conn.commit()
conn.close()

print("✅ Messages uploaded successfully!")
