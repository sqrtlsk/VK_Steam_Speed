import os
import re

def get_download_sizes(steam_path):
    download_path = os.path.join(steam_path, "steamapps", "downloading")
    sizes = {}
    if not os.path.exists(download_path):
        return sizes
    for folder in os.listdir(download_path):
        folder_path = os.path.join(download_path, folder)
        total_size = 0
        if os.path.isdir(folder_path):
            for root, dirs, files in os.walk(folder_path):
                for f in files:
                    try:
                        fp = os.path.join(root, f)
                        total_size += os.path.getsize(fp)
                    except:
                        pass
            sizes[folder] = total_size
    return sizes

def get_app_name(steam_path, appid):
    manifest_file = os.path.join(steam_path, "steamapps", f"appmanifest_{appid}.acf")
    if not os.path.exists(manifest_file):
        return f"AppID {appid}"
    try:
        with open(manifest_file, "r", encoding="utf-8") as f:
            content = f.read()
        match = re.search(r'"name"\s+"(.*?)"', content)
        if match:
            return match.group(1)
    except:
        pass
    return f"AppID {appid}"