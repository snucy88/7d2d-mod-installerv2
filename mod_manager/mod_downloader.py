import os
import requests
import xml.etree.ElementTree as ET

GITHUB_API_URL = "https://api.github.com"

def check_for_updates(mod):
    try:
        search_url = f"{GITHUB_API_URL}/search/repositories?q={mod['name']}"
        response = requests.get(search_url)
        if response.status_code == 200:
            items = response.json().get('items')
            if items:
                repo = items[0]  # Nehme das erste gefundene Repository
                latest_release_url = f"{GITHUB_API_URL}/repos/{repo['full_name']}/releases/latest"
                release_response = requests.get(latest_release_url)
                if release_response.status_code == 200:
                    latest_version = release_response.json().get('tag_name')
                    assets = release_response.json().get('assets', [])
                    download_url = assets[0]['browser_download_url'] if assets else None
                    return latest_version > mod['version'], download_url
        return False, None
    except Exception as e:
        print(f"Failed to check for updates for mod {mod['name']}: {e}")
        return False, None

def download_mod(mod, download_path, download_url):
    try:
        response = requests.get(download_url)
        if response.status_code == 200:
            mod_file_path = os.path.join(download_path, f"{mod['name']}.zip")
            with open(mod_file_path, 'wb') as file:
                file.write(response.content)
            return mod_file_path
        return None
    except Exception as e:
        print(f"Failed to download mod {mod['name']}: {e}")
        return None

def parse_mod_info(mod_info_path):
    try:
        tree = ET.parse(mod_info_path)
        root = tree.getroot()
        mod_info = {
            'name': root.find('Name').get('value') if root.find('Name') is not None else 'Unknown',
            'version': root.find('Version').get('value') if root.find('Version') is not None else 'Unknown',
            'author': root.find('Author').get('value') if root.find('Author') is not None else 'Unknown',
            'description': root.find('Description').get('value') if root.find('Description') is not None else 'No description'
        }
        return mod_info
    except ET.ParseError:
        print(f"Error parsing {mod_info_path}")
        return None
    except AttributeError as e:
        print(f"Missing attribute in {mod_info_path}: {e}")
        return None
