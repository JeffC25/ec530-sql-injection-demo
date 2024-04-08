from flask import Flask, send_file
from api import api
import sqlite3
import csv

app = Flask(__name__, template_folder='templates', static_folder='static')
app.register_blueprint(api, url_prefix='/api')

# Reset the database for demo
conn = sqlite3.connect('example.db')
c = conn.cursor()
c.execute('''DROP TABLE IF EXISTS users''')
c.execute('''CREATE TABLE IF NOT EXISTS users
             (id INTEGER PRIMARY KEY, username TEXT, name TEXT, birthday TEXT, secret TEXT, occupation TEXT, email TEXT, address TEXT, favorite_color TEXT, sleep_hours_per_night INTEGER, exercise_hours_per_week INTEGER, savings_amount REAL, total_tacos_eaten INTEGER)''')

# Load data from users.csv
with open('users.csv', 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        # id,username,name,birthday,secret,occupation,email,address,favorite_color,sleep_hours_per_night,exercise_hours_per_week,savings_amount,total_tacos_eaten
        c.execute("INSERT INTO users (username, name, birthday, secret, occupation, email, address, favorite_color, sleep_hours_per_night, exercise_hours_per_week, savings_amount, total_tacos_eaten) VALUES (?,?,?,?,?,?,?,?,?,?,?,?)", (row['username'], row['name'], row['birthday'], row['secret'], row['occupation'], row['email'], row['address'], row['favorite_color'], row['sleep_hours_per_night'], row['exercise_hours_per_week'], row['savings_amount'], row['total_tacos_eaten']))
conn.commit()
conn.close()

@app.route('/')
def index():
    return send_file('templates/index.html')

if __name__ == '__main__':
    app.run(debug=True)