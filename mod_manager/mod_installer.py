import zipfile
import shutil
import os

def install_mod(mod_zip_path, mods_path):
    with zipfile.ZipFile(mod_zip_path, 'r') as zip_ref:
        zip_ref.extractall(mods_path)

def remove_old_mod(mod_name, mods_path):
    mod_path = os.path.join(mods_path, mod_name)
    if os.path.exists(mod_path):
        shutil.rmtree(mod_path)
