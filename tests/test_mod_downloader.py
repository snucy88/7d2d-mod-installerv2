import unittest
from mod_manager.mod_downloader import check_for_updates, download_mod
import os

class TestModDownloader(unittest.TestCase):

    def test_check_for_updates(self):
        mod = {'name': 'example_mod', 'version': '1.0'}
        # Hier müsstest du die URL und die Logik anpassen
        self.assertFalse(check_for_updates(mod))

    def test_download_mod(self):
        mod = {'name': 'example_mod'}
        # Hier müsstest du die URL und die Logik anpassen
        self.assertFalse(download_mod(mod, "downloads"))

if __name__ == "__main__":
    unittest.main()
