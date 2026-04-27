# FastAPI System Info

Проект сделан в минимальном виде, чтобы быстрее реализовать основную функциональность: получить информацию о компьютере и вывести её на странице без перезагрузки.

Я не стал делать сложную архитектуру, выносить frontend в отдельные HTML/CSS/JS-файлы и добавлять стилизацию интерфейса, чтобы сохранить быструю реализацию задания.

Docker также не использовался как основной способ запуска, потому что при запуске приложения внутри контейнера backend будет получать информацию о системе контейнера, а не всегда о реальной системе пользователя.

Для запуска используется `uv`.


## Установка зависимостей
```bash
uv sync
```

## Запуск
```bash
uv run uvicorn main:app --reload
```

## Пример ответа
```json
{
    "os": {
        "system": "Linux",
        "version": "#1-NixOS SMP PREEMPT_DYNAMIC Sun Apr 12 20:48:06 UTC 2026",
        "platform": "Linux-7.0.0-x86_64-with-glibc2.42"
    },
    "cpu": {
        "processor": "Intel(R) Core(TM) i7-14650HX",
        "physical_cores": 16,
        "logical_cores": 24,
        "cpu_percent": 2.5
    },
    "memory": {
        "total_gb": 15.34,
        "used_gb": 9.53,
        "free_gb": 5.81,
        "percent": 62.1
    },
    "disks": [
        {
            "device": "/dev/nvme0n1p2",
            "mountpoint": "/",
            "filesystem": "ext4",
            "total_gb": 450.79,
            "used_gb": 63.63,
            "available_gb": 364.19,
            "percent": 14.9
        },
        {
            "device": "/dev/nvme0n1p2",
            "mountpoint": "/nix/store",
            "filesystem": "ext4",
            "total_gb": 450.79,
            "used_gb": 63.63,
            "available_gb": 364.19,
            "percent": 14.9
        },
        {
            "device": "/dev/nvme0n1p1",
            "mountpoint": "/boot",
            "filesystem": "vfat",
            "total_gb": 1,
            "used_gb": 0.1,
            "available_gb": 0.9,
            "percent": 10.2
        }
    ]
}
```
