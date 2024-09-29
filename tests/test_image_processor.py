import unittest
import os
import tempfile
from PIL import Image
import sys

# Add the src directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from image_processor import ImageProcessor

class TestImageProcessor(unittest.TestCase):
    def setUp(self):
        self.processor = ImageProcessor()
        self.test_dir = tempfile.mkdtemp()

    def tearDown(self):
        for file in os.listdir(self.test_dir):
            os.remove(os.path.join(self.test_dir, file))
        os.rmdir(self.test_dir)

    def create_test_image(self, size=(100, 100), color=(255, 0, 0), format='PNG'):
        image = Image.new('RGB', size, color)
        path = os.path.join(self.test_dir, f'test_image.{format.lower()}')
        image.save(path, format=format)
        return path

    def test_convert_to_favicon(self):
        input_path = self.create_test_image()
        output_path = os.path.join(self.test_dir, 'favicon.ico')
        sizes = [16, 32, 48]

        self.processor.convert_to_favicon(input_path, output_path, sizes)

        self.assertTrue(os.path.exists(output_path))
        with Image.open(output_path) as ico:
            self.assertEqual(ico.format, 'ICO')
            self.assertEqual(len(ico.info['sizes']), len(sizes))

    def test_resize_image(self):
        original_size = (100, 100)
        new_size = (50, 50)
        image = Image.new('RGBA', original_size, (255, 0, 0, 255))
        
        resized = self.processor.resize_image(image, new_size)
        
        self.assertEqual(resized.size, new_size)

    def test_validate_image(self):
        valid_path = self.create_test_image()
        invalid_path = os.path.join(self.test_dir, 'not_an_image.txt')
        
        with open(invalid_path, 'w') as f:
            f.write('This is not an image file.')

        self.assertTrue(self.processor.validate_image(valid_path))
        self.assertFalse(self.processor.validate_image(invalid_path))

if __name__ == '__main__':
    unittest.main()
