import os
import xml.etree.ElementTree as ET

def get_installed_mods(mods_path):
    mods = []
    for mod_name in os.listdir(mods_path):
        mod_info_path = os.path.join(mods_path, mod_name, "ModInfo.xml")
        if os.path.exists(mod_info_path):
            mod_info = parse_mod_info(mod_info_path)
            if mod_info:
                mods.append(mod_info)
    return mods

def parse_mod_info(mod_info_path):
    try:
        tree = ET.parse(mod_info_path)
        root = tree.getroot()
        mod_info = {
            'name': root.find('name').text,
            'version': root.find('version').text,
            'author': root.find('author').text,
            'description': root.find('description').text
        }
        return mod_info
    except ET.ParseError:
        print(f"Error parsing {mod_info_path}")
        return None
