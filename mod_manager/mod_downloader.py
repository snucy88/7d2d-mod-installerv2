import requests
import os

def check_for_updates(mod):
    # Beispiel-URL, die angepasst werden muss
    url = f"https://example.com/mods/{mod['name']}/latest"
    response = requests.get(url)
    if response.status_code == 200:
        latest_version = response.json()['version']
        return latest_version > mod['version']
    return False

def download_mod(mod, download_path):
    url = f"https://example.com/mods/{mod['name']}/download"
    response = requests.get(url)
    if response.status_code == 200:
        with open(os.path.join(download_path, f"{mod['name']}.zip"), 'wb') as file:
            file.write(response.content)
        return True
    return False
