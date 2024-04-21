import sqlite3

# Connect to SQLite database
conn = sqlite3.connect('scraped_data.db')
cursor = conn.cursor()

# Create a table to store scraped data
cursor.execute('''
    CREATE TABLE IF NOT EXISTS scraped_data (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        url TEXT,
        content TEXT
    )
''')

# Commit changes and close connection
conn.commit()
conn.close()
