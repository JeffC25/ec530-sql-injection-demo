from flask import Flask, send_file
from api import api
import sqlite3
import csv

app = Flask(__name__, template_folder='templates', static_folder='static')
app.register_blueprint(api, url_prefix='/api')

@app.route('/')
def index():
    return send_file('templates/index.html')

if __name__ == '__main__':
    app.run(debug=True)