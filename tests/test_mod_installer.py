import unittest
from mod_manager.mod_installer import install_mod, remove_old_mod
import os
import zipfile

class TestModInstaller(unittest.TestCase):

    def setUp(self):
        self.mod_zip_path = "dummy_mod.zip"
        self.mods_path = "mods_directory"
        os.makedirs(self.mods_path, exist_ok=True)

        # Erstelle eine echte Dummy-Zip-Datei
        with zipfile.ZipFile(self.mod_zip_path, 'w') as zipf:
            zipf.writestr('mod_name/', '')

    def tearDown(self):
        if os.path.exists(self.mod_zip_path):
            os.remove(self.mod_zip_path)
        if os.path.exists(self.mods_path):
            os.rmdir(self.mods_path)

    def test_install_mod(self):
        install_mod(self.mod_zip_path, self.mods_path)
        self.assertTrue(os.path.exists(os.path.join(self.mods_path, 'mod_name')))

    def test_remove_old_mod(self):
        mod_name = "example_mod"
        mod_path = os.path.join(self.mods_path, mod_name)
        os.makedirs(mod_path, exist_ok=True)
        remove_old_mod(mod_name, self.mods_path)
        self.assertFalse(os.path.exists(mod_path))

if __name__ == "__main__":
    unittest.main()
