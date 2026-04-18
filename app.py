from flask import Flask, render_template, request
from emotion_detection import emotion_detector

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/detect", methods=["POST"])
def detect():
    text = request.form.get("text")
    result = emotion_detector(text)
    return render_template("index.html", result=result, text=text)

@app.errorhandler(404)
def not_found(e):
    return render_template("index.html", result={"error": "Page Not Found"}), 404

@app.errorhandler(500)
def server_error(e):
    return render_template("index.html", result={"error": "Server Error"}), 500


# IMPORTANT FOR LAB ENVIRONMENT
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)