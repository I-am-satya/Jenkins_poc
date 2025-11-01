from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, Satya! Your Flask app is running via Jenkins and Docker."

@app.route('/health')
def health():
    return {"status": "UP"}, 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

