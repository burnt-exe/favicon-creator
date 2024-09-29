import unittest
import sys
import os

# Add the src directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

import favicon_creator

class TestFaviconCreatorInit(unittest.TestCase):
    def test_version(self):
        self.assertIsNotNone(favicon_creator.__version__)
        self.assertIsInstance(favicon_creator.__version__, str)

    def test_imports(self):
        self.assertTrue(hasattr(favicon_creator, 'FaviconCreator'))
        self.assertTrue(hasattr(favicon_creator, 'ImageProcessor'))
        self.assertTrue(hasattr(favicon_creator, 'FaviconCreatorGUI'))

    def test_default_sizes(self):
        self.assertIsInstance(favicon_creator.DEFAULT_SIZES, list)
        self.assertTrue(all(isinstance(size, tuple) for size in favicon_creator.DEFAULT_SIZES))

    def test_main_function(self):
        self.assertTrue(hasattr(favicon_creator, 'main'))
        self.assertTrue(callable(favicon_creator.main))

if __name__ == '__main__':
    unittest.main()
