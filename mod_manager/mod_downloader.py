import os
import requests
import xml.etree.ElementTree as ET

def check_for_updates(mod):
    try:
        update_url = mod.get('update_url')
        response = requests.get(update_url)
        if response.status_code == 200:
            latest_version = response.json().get('version')
            return latest_version > mod['version']
        return False
    except Exception as e:
        print(f"Failed to check for updates for mod {mod['name']}: {e}")
        return False

def download_mod(mod, download_path):
    try:
        download_url = mod.get('download_url')
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
            'name': root.find('name').text if root.find('name') is not None else 'Unknown',
            'version': root.find('version').text if root.find('version') is not None else 'Unknown',
            'author': root.find('author').text if root.find('author') is not None else 'Unknown',
            'description': root.find('description').text if root.find('description') is not None else 'No description',
            'update_url': root.find('update_url').text if root.find('update_url') is not None else '',
            'download_url': root.find('download_url').text if root.find('download_url') is not None else ''
        }
        return mod_info
    except ET.ParseError:
        print(f"Error parsing {mod_info_path}")
        return None
    except AttributeError as e:
        print(f"Missing attribute in {mod_info_path}: {e}")
        return None
