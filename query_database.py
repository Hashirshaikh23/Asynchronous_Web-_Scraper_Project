import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('scraped_data.db')

# Create a cursor object to execute SQL queries
cursor = conn.cursor()

# Execute a SELECT query to retrieve data
cursor.execute('SELECT * FROM scraped_data')

# Fetch the results
results = cursor.fetchall()

# Print the results
for row in results:
    print(row)

# Close the connection
conn.close()
