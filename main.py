from steam_path import get_steam_path
from monitor import monitor_downloads

if __name__ == "__main__":
    steam_path = get_steam_path()
    if steam_path:
        monitor_downloads(steam_path, duration_minutes=5, interval_seconds=60)
    else:
        print("Не удалось определить путь установки Steam")
