import unittest
from unittest.mock import patch, MagicMock
from mod_manager.mod_downloader import check_for_updates, download_mod
import os

class TestModDownloader(unittest.TestCase):

    @patch('mod_manager.mod_downloader.requests.get')
    def test_check_for_updates(self, mock_get):
        # Mock die Antwort für die Suche nach Repositories
        mock_search_response = MagicMock()
        mock_search_response.status_code = 200
        mock_search_response.json.return_value = {
            'items': [{'full_name': 'example/example_mod'}]
        }

        # Mock die Antwort für die neueste Release
        mock_release_response = MagicMock()
        mock_release_response.status_code = 200
        mock_release_response.json.return_value = {
            'tag_name': '2.0',
            'assets': [{'browser_download_url': 'http://example.com/mod.zip'}]
        }

        # Reihenfolge der Mock-Rückgaben festlegen
        mock_get.side_effect = [mock_search_response, mock_release_response]

        mod = {'name': 'example_mod', 'version': '1.0'}
        update_available, download_url = check_for_updates(mod)
        self.assertTrue(update_available)
        self.assertIsNotNone(download_url)

        mod = {'name': 'example_mod', 'version': '2.0'}
        update_available, download_url = check_for_updates(mod)
        self.assertFalse(update_available)
        self.assertIsNotNone(download_url)

    @patch('mod_manager.mod_downloader.requests.get')
    def test_download_mod(self, mock_get):
        # Mock die Antwort für den Mod-Download
        mock_download_response = MagicMock()
        mock_download_response.status_code = 200
        mock_download_response.content = b'Test content'

        # Reihenfolge der Mock-Rückgaben festlegen
        mock_get.side_effect = [mock_download_response]

        mod = {'name': 'example_mod'}
        download_path = 'downloads'
        os.makedirs(download_path, exist_ok=True)

        download_url = "http://example.com/mod.zip"
        mod_file_path = download_mod(mod, download_path, download_url)
        self.assertIsNotNone(mod_file_path)
        self.assertTrue(os.path.exists(mod_file_path))

        with open(mod_file_path, 'rb') as file:
            self.assertEqual(file.read(), b'Test content')

        # Bereinigen
        os.remove(mod_file_path)
        os.rmdir(download_path)

if __name__ == "__main__":
    unittest.main()
