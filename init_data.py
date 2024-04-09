import csv
import sqlite3

# Create a connection to the database
conn = sqlite3.connect('example.db')
c = conn.cursor()

# Reset the database for demo
c.execute('''DROP TABLE IF EXISTS users''')

# Create the users table
c.execute('''CREATE TABLE IF NOT EXISTS users (
             id INTEGER PRIMARY KEY AUTOINCREMENT,
             username TEXT UNIQUE NOT NULL,
             name TEXT,
             birthday TEXT,
             secret TEXT,
             occupation TEXT,
             email TEXT,
             address TEXT,
             favorite_color TEXT,
             sleep_hours_per_night INTEGER,
             exercise_hours_per_week INTEGER,
             savings_amount INTEGER,
             total_tacos_eaten INTEGER
             )''')

# Load data from users.csv
with open('users.csv', 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        # print("Inserting user:", row['username'])
        c.execute("INSERT INTO users (username, name, birthday, secret, occupation, email, address, favorite_color, sleep_hours_per_night, exercise_hours_per_week, savings_amount, total_tacos_eaten) VALUES (?,?,?,?,?,?,?,?,?,?,?,?)", (row['username'], row['name'], row['birthday'], row['secret'], row['occupation'], row['email'], row['address'], row['favorite_color'], row['sleep_hours_per_night'], row['exercise_hours_per_week'], row['savings_amount'], row['total_tacos_eaten']))

# Commit the changes and close the connection
conn.commit()
conn.close()