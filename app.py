from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Welcome to Skyage IT Services Pvt Ltd'

@app.route('/health')
def health():
    return 'Server is up and running'
