import platform
import os

def get_steam_path():
    system = platform.system()
    if system == "Windows":
        import winreg
        try:
            key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"Software\Valve\Steam")
            steam_path, _ = winreg.QueryValueEx(key, "SteamPath")
            return steam_path
        except:
            return None
    elif system == "Darwin":
        return os.path.expanduser("~/Library/Application Support/Steam")
    elif system == "Linux":
        return os.path.expanduser("~/.steam/steam")
    else:
        return None