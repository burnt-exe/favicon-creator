import os
from PIL import Image
import logging

class ImageProcessor:
    def __init__(self):
        self.logger = logging.getLogger(__name__)

    def convert_to_favicon(self, input_path, output_path, sizes, progress_callback=None):
        """
        Convert an image to ICO format with multiple sizes.

        :param input_path: Path to the input image file
        :param output_path: Path where the favicon will be saved
        :param sizes: List of sizes for the favicon (e.g., [16, 32, 48, 64])
        :param progress_callback: Optional callback function to report progress
        """
        try:
            self.logger.info(f"Starting conversion: {input_path} -> {output_path}")
            
            # Open the original image
            with Image.open(input_path) as img:
                # Convert image to RGBA if it's not already
                if img.mode != 'RGBA':
                    img = img.convert('RGBA')

                # Create a list to store different sizes of the image
                icon_sizes = [(size, size) for size in sizes]
                icons = []

                for i, size in enumerate(icon_sizes):
                    # Resize the image
                    resized_img = self.resize_image(img, size)
                    icons.append(resized_img)

                    if progress_callback:
                        progress = (i + 1) / len(icon_sizes) * 100
                        progress_callback(progress)

                # Save the favicon
                icons[0].save(output_path, format='ICO', sizes=icon_sizes, append_images=icons[1:])

            self.logger.info(f"Conversion completed: {output_path}")

        except Exception as e:
            self.logger.error(f"Error during conversion: {str(e)}")
            raise

    def resize_image(self, img, size):
        """
        Resize an image to a specific size while maintaining aspect ratio and filling with transparency.

        :param img: PIL Image object
        :param size: Tuple of (width, height)
        :return: Resized PIL Image object
        """
        img_ratio = img.width / img.height
        target_ratio = size[0] / size[1]
        
        if img_ratio > target_ratio:
            # Image is wider than target, fit to height
            resize_height = size[1]
            resize_width = int(resize_height * img_ratio)
        else:
            # Image is taller than target, fit to width
            resize_width = size[0]
            resize_height = int(resize_width / img_ratio)

        resized_img = img.resize((resize_width, resize_height), Image.LANCZOS)

        # Create a new transparent image of the target size
        new_img = Image.new('RGBA', size, (0, 0, 0, 0))

        # Paste the resized image onto the center of the new image
        paste_x = (size[0] - resize_width) // 2
        paste_y = (size[1] - resize_height) // 2
        new_img.paste(resized_img, (paste_x, paste_y))

        return new_img

    def validate_image(self, file_path):
        """
        Validate if the given file is a supported image format.

        :param file_path: Path to the image file
        :return: Boolean indicating if the file is a valid image
        """
        try:
            with Image.open(file_path) as img:
                img.verify()
            return True
        except Exception as e:
            self.logger.warning(f"Invalid image file: {file_path}. Error: {str(e)}")
            return False

    def get_image_info(self, file_path):
        """
        Get information about the image file.

        :param file_path: Path to the image file
        :return: Dictionary containing image information
        """
        try:
            with Image.open(file_path) as img:
                info = {
                    "format": img.format,
                    "mode": img.mode,
                    "size": img.size,
                }
                return info
        except Exception as e:
            self.logger.error(f"Error getting image info: {str(e)}")
            return None

if __name__ == "__main__":
    # Set up logging
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

    # Test the ImageProcessor
    processor = ImageProcessor()
    
    # Example usage
    input_path = "path/to/your/input/image.png"
    output_path = "path/to/your/output/favicon.ico"
    sizes = [16, 32, 48, 64]

    if processor.validate_image(input_path):
        info = processor.get_image_info(input_path)
        print(f"Image info: {info}")

        def progress_callback(progress):
            print(f"Conversion progress: {progress:.2f}%")

        try:
            processor.convert_to_favicon(input_path, output_path, sizes, progress_callback)
            print("Conversion completed successfully!")
        except Exception as e:
            print(f"Conversion failed: {str(e)}")
    else:
        print("Invalid image file.")
