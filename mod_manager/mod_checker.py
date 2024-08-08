import os
import xml.etree.ElementTree as ET

def get_installed_mods(mods_path):
    mods = []
    for mod_name in os.listdir(mods_path):
        mod_dir_path = os.path.join(mods_path, mod_name)
        mod_info_path = os.path.join(mod_dir_path, "ModInfo.xml")
        if os.path.exists(mod_info_path):
            print(f"Parsing mod info: {mod_info_path}")
            mod_info = parse_mod_info(mod_info_path)
            if mod_info:
                mods.append(mod_info)
            else:
                print(f"Failed to parse mod info: {mod_info_path}")
        else:
            print(f"ModInfo.xml not found: {mod_info_path}")
    return mods

def parse_mod_info(mod_info_path):
    try:
        tree = ET.parse(mod_info_path)
        root = tree.getroot()
        mod_info = {
            'name': root.find('name').text if root.find('name') is not None else 'Unknown',
            'version': root.find('version').text if root.find('version') is not None else 'Unknown',
            'author': root.find('author').text if root.find('author') is not None else 'Unknown',
            'description': root.find('description').text if root.find('description') is not None else 'No description'
        }
        return mod_info
    except ET.ParseError:
        print(f"Error parsing {mod_info_path}")
        return None
    except AttributeError as e:
        print(f"Missing attribute in {mod_info_path}: {e}")
        return None
