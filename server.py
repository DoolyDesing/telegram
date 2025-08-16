from flask import Flask, send_from_directory

app = Flask(__name__, static_folder="dist")

@app.get("/")
def index():
    return send_from_directory(app.static_folder, "index.html")

@app.get("/hello")
def hello():
    return "<h1>Привет из Flask!</h1>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
