import unittest
from mod_manager.mod_installer import install_mod, remove_old_mod
import os

class TestModInstaller(unittest.TestCase):

    def test_install_mod(self):
        # Du kannst einen Dummy-Mod zum Testen verwenden
        mod_zip_path = "path_to_mod_zip"  # Passe diesen Pfad an
        mods_path = "path_to_mods_directory"  # Passe diesen Pfad an
        install_mod(mod_zip_path, mods_path)
        self.assertTrue(os.path.exists(os.path.join(mods_path, "mod_name")))  # Passe diesen Pfad an

    def test_remove_old_mod(self):
        mod_name = "example_mod"
        mods_path = "path_to_mods_directory"  # Passe diesen Pfad an
        remove_old_mod(mod_name, mods_path)
        self.assertFalse(os.path.exists(os.path.join(mods_path, mod_name)))

if __name__ == "__main__":
    unittest.main()
