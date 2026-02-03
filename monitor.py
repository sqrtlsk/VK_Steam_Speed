import time
from steam_utils import get_download_sizes, get_app_name

def monitor_downloads(steam_path, duration_minutes=5, interval_seconds=60):
    prev_sizes = get_download_sizes(steam_path)

    if not prev_sizes:
        print("Активных загрузок НЕТ — все игры загружены или загрузка на паузе")
    else:
        for appid, size in prev_sizes.items():
            game_name = get_app_name(steam_path, appid)
            print(f"Игра: {game_name} | ")

    iterations = duration_minutes
    for _ in range(iterations):
        time.sleep(interval_seconds)
        new_sizes = get_download_sizes(steam_path)

        if not new_sizes:
            print("Активных загрузок НЕТ — все игры загружены или загрузка на паузе")
        else:
            for appid, new_size in new_sizes.items():
                prev_size = prev_sizes.get(appid, 0)
                speed_mb_s = (new_size - prev_size) / interval_seconds / (1024*1024)
                game_name = get_app_name(steam_path, appid)
                if speed_mb_s <= 0:
                    print(f"Игра: {game_name} | загрузка ПРИОСТАНОВЛЕНА")
                else:
                    print(f"Игра: {game_name} | Скорость: {speed_mb_s:.2f} MB/s")
        prev_sizes = new_sizes
