from flask import Flask, jsonify

app = Flask(__name__)

@app.get("/")
def root():
    return "<h1>Hello World v13</h1>"

@app.get("/api/v1/details")
def details():
    return jsonify({"message": "hello_world"})

@app.get("/api/v1/healthz")
def health():
    return jsonify({"status": "up"}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
