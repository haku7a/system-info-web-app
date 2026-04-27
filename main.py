from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import platform
import psutil

app = FastAPI()

def get_processor_name():
    processor = platform.processor()

    if processor:
        return processor

    try:
        with open("/proc/cpuinfo", "r", encoding="utf-8") as file:
            for line in file:
                if line.startswith("model name"):
                    return line.split(":", 1)[1].strip()
    except FileNotFoundError:
        pass

    return "Unknown processor"



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
    memory = psutil.virtual_memory()

    disks = []

    for disk in psutil.disk_partitions():
        try:
            usage = psutil.disk_usage(disk.mountpoint)

            disks.append({
                "device": disk.device,
                "mountpoint": disk.mountpoint,
                "filesystem": disk.fstype,
                "total_gb": round(usage.total / 1024 ** 3, 2),
                "used_gb": round(usage.used / 1024 ** 3, 2),
                "available_gb": round(usage.free / 1024 ** 3, 2),
                "percent": usage.percent
            })
        except PermissionError:
            continue

    return {
        "os": {
            "system": platform.system(),
            "version": platform.version(),
            "platform": platform.platform()
        },
        "cpu": {
            "processor": get_processor_name(),
            "physical_cores": psutil.cpu_count(logical=False),
            "logical_cores": psutil.cpu_count(logical=True),
            "cpu_percent": psutil.cpu_percent(interval=1)
        },
        "memory": {
            "total_gb": round(memory.total / 1024 ** 3, 2),
            "used_gb": round(memory.used / 1024 ** 3, 2),
            "free_gb": round(memory.available / 1024 ** 3, 2),
            "percent": memory.percent
        },
        "disks": disks

            }
