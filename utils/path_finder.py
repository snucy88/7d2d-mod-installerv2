import os
import winreg

def find_7d2d_install_path():
    steam_path = get_steam_install_path()
    if not steam_path:
        raise FileNotFoundError("Steam installation not found.")
    
    library_folders = get_steam_library_folders(steam_path)
    for folder in library_folders:
        potential_path = os.path.join(folder, "steamapps", "common", "7 Days To Die")
        if os.path.exists(potential_path):
            return potential_path
    
    raise FileNotFoundError("7 Days To Die installation not found.")

def get_steam_install_path():
    try:
        key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\Valve\Steam")
        value, _ = winreg.QueryValueEx(key, "InstallPath")
        return value
    except FileNotFoundError:
        return None

def get_steam_library_folders(steam_path):
    library_folders = [steam_path]
    library_folders_file = os.path.join(steam_path, "steamapps", "libraryfolders.vdf")
    if os.path.exists(library_folders_file):
        with open(library_folders_file, 'r') as file:
            for line in file:
                if "path" in line:
                    path = line.split('"')[3]
                    library_folders.append(path)
    return library_folders
