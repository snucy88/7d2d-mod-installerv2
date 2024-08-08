import unittest
from utils.path_finder import find_7d2d_install_path

class TestPathFinder(unittest.TestCase):

    def test_find_7d2d_install_path(self):
        path = find_7d2d_install_path()
        self.assertTrue(path is not None, "7 Days to Die installation not found")

if __name__ == "__main__":
    unittest.main()
