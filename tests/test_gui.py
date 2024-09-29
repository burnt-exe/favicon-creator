import unittest
from unittest.mock import Mock, patch
import tkinter as tk
import sys
import os

# Add the src directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from gui import FaviconCreatorGUI

class TestFaviconCreatorGUI(unittest.TestCase):
    def setUp(self):
        self.root = tk.Tk()
        self.mock_image_processor = Mock()
        self.gui = FaviconCreatorGUI(self.root, self.mock_image_processor)

    def tearDown(self):
        self.root.destroy()

    def test_initial_state(self):
        self.assertEqual(self.gui.file_entry.get(), "")
        self.assertEqual(self.gui.save_entry.get(), "")
        self.assertEqual(self.gui.size_var.get(), "16,32,48,64")
        self.assertEqual(self.gui.status_var.get(), "Ready")

    @patch('tkinter.filedialog.askopenfilename')
    def test_browse_file(self, mock_askopenfilename):
        mock_askopenfilename.return_value = "/path/to/image.png"
        self.gui.browse_file()
        self.assertEqual(self.gui.file_entry.get(), "/path/to/image.png")
        self.assertIn("Selected file: image.png", self.gui.status_var.get())

    @patch('tkinter.filedialog.askdirectory')
    def test_browse_save_location(self, mock_askdirectory):
        mock_askdirectory.return_value = "/path/to/save"
        self.gui.browse_save_location()
        self.assertEqual(self.gui.save_entry.get(), "/path/to/save")
        self.assertIn("Save location: /path/to/save", self.gui.status_var.get())

    @patch('gui.messagebox.showwarning')
    def test_convert_to_favicon_missing_info(self, mock_showwarning):
        self.gui.convert_to_favicon()
        mock_showwarning.assert_called_once_with("Missing Information", "Please select both an input file and save location.")

    @patch('gui.messagebox.showinfo')
    def test_convert_to_favicon_success(self, mock_showinfo):
        self.gui.file_entry.insert(0, "/path/to/input.png")
        self.gui.save_entry.insert(0, "/path/to/save")
        self.gui.size_var.set("16,32,48")

        self.gui.convert_to_favicon()

        self.mock_image_processor.convert_to_favicon.assert_called_once()
        mock_showinfo.assert_called_once()
        self.assertIn("Conversion complete", self.gui.status_var.get())

if __name__ == '__main__':
    unittest.main()
