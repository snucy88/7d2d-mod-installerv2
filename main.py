import os
import logging
from utils.path_finder import find_7d2d_install_path
from mod_manager.mod_checker import get_installed_mods
from mod_manager.mod_downloader import check_for_updates, download_mod
from mod_manager.mod_installer import install_mod, remove_old_mod

logging.basicConfig(level=logging.INFO)

def main():
    try:
        game_path = find_7d2d_install_path()
        mods_path = os.path.join(game_path, "Mods")
        download_path = os.path.join(game_path, "downloads")
        os.makedirs(download_path, exist_ok=True)
        
        installed_mods = get_installed_mods(mods_path)
        
        for mod in installed_mods:
            logging.info(f"Checking for updates for mod: {mod['name']}")
            if check_for_updates(mod):
                logging.info(f"Update available for {mod['name']}, downloading...")
                mod_file_path = download_mod(mod, download_path)
                if mod_file_path:
                    logging.info(f"Downloaded {mod['name']}, installing...")
                    remove_old_mod(mod['name'], mods_path)
                    install_mod(mod_file_path, mods_path)
                    logging.info(f"Updated {mod['name']} to the latest version")
            else:
                logging.info(f"{mod['name']} is up to date")
    except FileNotFoundError as e:
        logging.error(e)

if __name__ == "__main__":
    main()
