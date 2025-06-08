from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "✅ FunSpeak 后端部署成功！"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
