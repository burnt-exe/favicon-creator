import unittest
from unittest.mock import patch, MagicMock
import sys
import os

# Add the src directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from favicon_creator import FaviconCreator

class TestFaviconCreator(unittest.TestCase):
    @patch('favicon_creator.ImageProcessor')
    @patch('favicon_creator.FaviconCreatorGUI')
    def setUp(self, mock_gui, mock_processor):
        self.mock_root = MagicMock()
        self.mock_processor = mock_processor.return_value
        self.mock_gui = mock_gui.return_value
        self.app = FaviconCreator(self.mock_root)

    def test_initialization(self):
        self.assertIsNotNone(self.app.image_processor)
        self.assertIsNotNone(self.app.gui)

    def test_run(self):
        self.app.run()
        self.mock_root.mainloop.assert_called_once()

    @patch('favicon_creator.messagebox')
    def test_convert_to_favicon(self, mock_messagebox):
        # Simulate successful conversion
        self.app.convert_to_favicon('input.png', 'output.ico', [16, 32])
        self.mock_processor.convert_to_favicon.assert_called_once_with('input.png', 'output.ico', [16, 32], self.app.update_progress)
        mock_messagebox.showinfo.assert_called_once()

        # Simulate conversion error
        self.mock_processor.convert_to_favicon.side_effect = Exception("Test error")
        self.app.convert_to_favicon('input.png', 'output.ico', [16, 32])
        mock_messagebox.showerror.assert_called_once()

    def test_update_progress(self):
        self.app.update_progress(50)
        self.mock_gui.update_progress.assert_called_once_with(50)

if __name__ == '__main__':
    unittest.main()
