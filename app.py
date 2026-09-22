import os
from flask import Flask, render_template_string

app = Flask(__name__)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <title>Web Application version 2.1.7</title>
    <style>
        body { font-family: Arial, sans-serif; background-color: #f4f6f9; display: flex; justify-content: center; align-items: center; height: 100vh; margin: 0; }
        .card { background: white; padding: 30px; border-radius: 10px; box-shadow: 0 4px 15px rgba(0,0,0,0.1); text-align: center; max-width: 500px; width: 100%; }
        h1 { color: #2c3e50; font-size: 24px; margin-bottom: 10px; }
        p { color: #7f8c8d; margin-bottom: 20px; }
        .secret-box { background: #eef2f7; border-left: 4px solid #3498db; padding: 15px; border-radius: 4px; text-align: left; word-break: break-all; }
        .secret-title { font-weight: bold; color: #34495e; font-size: 12px; text-transform: uppercase; margin-bottom: 5px; }
        .secret-value { font-family: monospace; font-size: 16px; color: #e74c3c; }
    </style>
</head>
<body>
    <div class="card">
        <h1>🚀 Web Application</h1>
        <p>Приложение запущено за Nginx реверс-прокси</p>
        <div class="secret-box">
            <div class="secret-title">Загруженный секрет (Secret Manager / K8s Secret):</div>
            <div class="secret-value">{{ secret_value }}</div>
        </div>
    </div>
</body>
</html>
"""

@app.route("/")
def index():
    secret_value = os.getenv("APP_SECRET", "Секрет не найден!")
    return render_template_string(HTML_TEMPLATE, secret_value=secret_value)

@app.route("/healthz")
def healthz():
    return "OK", 200

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000)
