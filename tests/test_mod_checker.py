import unittest
from mod_manager.mod_checker import get_installed_mods

class TestModChecker(unittest.TestCase):

    def test_get_installed_mods(self):
        mods = get_installed_mods("path_to_mods_directory")  # Passe diesen Pfad an
        self.assertIsInstance(mods, list)

if __name__ == "__main__":
    unittest.main()
