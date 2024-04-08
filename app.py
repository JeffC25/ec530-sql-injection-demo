from flask import Flask, send_file
from api import api

app = Flask(__name__)
app.register_blueprint(api, url_prefix='/api')

@app.route('/')
def index():
    return send_file('templates/index.html')

if __name__ == '__main__':
    app.run(debug=True)