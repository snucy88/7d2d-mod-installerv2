from utils.path_finder import find_7d2d_install_path
from mod_manager.mod_checker import get_installed_mods
from mod_manager.mod_downloader import check_for_updates, download_mod
from mod_manager.mod_installer import install_mod, remove_old_mod

def main():
    try:
        game_path = find_7d2d_install_path()
        mods_path = os.path.join(game_path, "Mods")
        
        installed_mods = get_installed_mods(mods_path)
        
        for mod in installed_mods:
            if check_for_updates(mod):
                print(f"Update available for {mod['name']}")
                if download_mod(mod, "downloads"):
                    remove_old_mod(mod['name'], mods_path)
                    install_mod(os.path.join("downloads", f"{mod['name']}.zip"), mods_path)
                    print(f"Updated {mod['name']} to the latest version")
            else:
                print(f"{mod['name']} is up to date")
    except FileNotFoundError as e:
        print(e)

if __name__ == "__main__":
    main()
