from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, Boss! Your Flask app is running successfully on Azure!"

@app.route('/about')
def about():
    return "This is a simple Flask application hosted on Azure Web App."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
