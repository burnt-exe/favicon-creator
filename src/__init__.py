"""
Favicon Creator

A Python package for creating favicons from various image formats.

This package provides tools to convert images to favicon format (.ico),
resize images, and handle various image processing tasks related to
favicon creation.

Modules:
    gui: Contains the graphical user interface for the Favicon Creator application.
    image_processor: Provides core image processing functionality.
    utils: Contains utility functions used across the package.

Classes:
    FaviconCreatorApp: Main application class for the GUI.
    ImageProcessor: Handles image conversion and processing.

Functions:
    create_favicon: Converts an image to favicon format.
    resize_image: Resizes an image while maintaining aspect ratio.
    get_version: Returns the current version of the package.

Constants:
    __version__: The current version of the Favicon Creator package.
    DEFAULT_SIZES: Default sizes for favicon generation.

For more information, please refer to the documentation at:
https://github.com/burnt-exe/favicon-creator/docs
"""

# Version of the favicon-creator package
__version__ = "0.1.0"

# Standard library imports
import os
import sys

# Local imports
from .gui import FaviconCreatorApp
from .image_processor import ImageProcessor, create_favicon, resize_image
from .utils import get_version, setup_logging

# Default sizes for favicon generation
DEFAULT_SIZES = [(16, 16), (32, 32), (48, 48), (64, 64)]

# Setup logging for the package
setup_logging()

def main():
    """
    Main entry point for the Favicon Creator application.
    Launches the graphical user interface.
    """
    root = FaviconCreatorApp()
    root.mainloop()

# Convenience function to create a favicon from the command line
def cli_create_favicon(input_path, output_path, sizes=DEFAULT_SIZES):
    """
    Creates a favicon from the command line.

    Args:
        input_path (str): Path to the input image file.
        output_path (str): Path where the favicon will be saved.
        sizes (list of tuples): List of sizes for the favicon. Defaults to DEFAULT_SIZES.

    Returns:
        bool: True if favicon was created successfully, False otherwise.
    """
    try:
        create_favicon(input_path, output_path, sizes)
        print(f"Favicon created successfully: {output_path}")
        return True
    except Exception as e:
        print(f"Error creating favicon: {str(e)}")
        return False

# If the script is run directly, launch the GUI application
if __name__ == "__main__":
    main()

# Define what should be imported with "from favicon_creator import *"
__all__ = ['FaviconCreatorApp', 'ImageProcessor', 'create_favicon', 'resize_image',
           'get_version', 'DEFAULT_SIZES', 'cli_create_favicon']
