import unittest
from mod_manager.mod_checker import get_installed_mods
from utils.path_finder import find_7d2d_install_path
import os

class TestModChecker(unittest.TestCase):

    def test_get_installed_mods(self):
        game_path = find_7d2d_install_path()
        mods_path = os.path.join(game_path, "Mods")
        mods = get_installed_mods(mods_path)
        self.assertIsInstance(mods, list)

if __name__ == "__main__":
    unittest.main()
