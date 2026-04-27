from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import platform

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def frontend():
    return """
    <!DOCTYPE html>
    <html lang="ru">
    <head>
        <meta charset="UTF-8">
        <title>Информация о компьютере</title>
    </head>
    <body>

        <button onclick="loadInfo()">Инфо</button>

        <pre id="result"></pre>

        <script>
            async function loadInfo() {
                const response = await fetch('/api/info/');
                const data = await response.json();

                document.getElementById('result').textContent =
                    JSON.stringify(data, null, 4);
            }
        </script>
    </body>
    </html>
    """




@app.get("/api/info/")
def get_info():
    return {
        "os": {
            "system": platform.system(),
            "version": platform.version(),
            "platform": platform.platform()
        },

            }
