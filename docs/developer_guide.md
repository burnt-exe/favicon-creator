# Favicon Creator Developer Guide

<p align="center">
  <img src="https://github.com/burnt-exe/favicon-creator/raw/89643f237aa756df4a0b80b6fb276e81ad209c18/assets/fiiltered.png" alt="Skunkworks Projects Logo" width="200"/>
</p>

<p align="center">
  <strong>Welcome to the Favicon Creator Developer Guide!</strong>
</p>

## Table of Contents

1. [Introduction](#introduction)
2. [Project Structure](#project-structure)
3. [Setting Up the Development Environment](#setting-up-the-development-environment)
4. [Coding Standards](#coding-standards)
5. [GUI Development](#gui-development)
6. [Image Processing](#image-processing)
7. [Testing](#testing)
8. [Documentation](#documentation)
9. [Version Control and Git Workflow](#version-control-and-git-workflow)
10. [Continuous Integration and Deployment](#continuous-integration-and-deployment)
11. [Contributing](#contributing)
12. [Troubleshooting](#troubleshooting)

## 1. Introduction

Welcome to the Favicon Creator project! This guide is designed to help developers understand the project structure, set up their development environment, and contribute effectively to the project.

### Project Overview

Favicon Creator is a Python-based GUI application that allows users to easily convert various image formats into favicons. Our goal is to provide a user-friendly tool for website developers and designers to quickly create professional-looking favicons.

<p align="center">
  <img src="https://github.com/burnt-exe/favicon-creator/raw/89643f237aa756df4a0b80b6fb276e81ad209c18/assets/fiiltered.ico" alt="Favicon Creator Icon" width="32"/>
</p>

## 2. Project Structure

Our project follows a modular structure to enhance maintainability and scalability:

```
favicon-creator/
├── src/
│   ├── favicon_creator/
│   │   ├── __init__.py
│   │   ├── main.py
│   │   ├── gui.py
│   │   └── image_processor.py
│   └── tests/
│       ├── __init__.py
│       ├── test_gui.py
│       └── test_image_processor.py
├── assets/
│   ├── fiiltered.ico
│   └── fiiltered.png
├── docs/
│   ├── user_guide.md
│   └── developer_guide.md
├── .github/
│   └── workflows/
│       └── ci.yml
├── .gitignore
├── LICENSE
├── README.md
├── requirements.txt
└── setup.py
```

## 3. Setting Up the Development Environment

To set up your development environment:

1. Clone the repository:
   ```
   git clone https://github.com/burnt-exe/favicon-creator.git
   cd favicon-creator
   ```

2. Create a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Install the package in editable mode:
   ```
   pip install -e .
   ```

## 4. Coding Standards

We follow the PEP 8 style guide for Python code. Some key points:

- Use 4 spaces for indentation
- Limit lines to 79 characters
- Use snake_case for function and variable names
- Use CamelCase for class names
- Write docstrings for all public modules, functions, classes, and methods

We use `flake8` for linting and `black` for code formatting. Run these before committing:

```
flake8 src tests
black src tests
```

## 5. GUI Development

The GUI is built using Tkinter and ttkthemes. Key files:

- `src/favicon_creator/gui.py`: Contains the main application window and UI components

When adding new UI elements:

1. Use ttk widgets for a consistent look
2. Follow the existing layout structure
3. Implement event handlers in the same class as the UI elements they correspond to
4. Use grid geometry manager for layout

Example of adding a new button:

```python
import tkinter as tk
from tkinter import ttk

class FaviconCreatorApp:
    def __init__(self, master):
        self.master = master
        self.create_widgets()

    def create_widgets(self):
        # ... existing widgets ...
        
        self.new_button = ttk.Button(self.master, text="New Feature", command=self.new_feature)
        self.new_button.grid(row=5, column=0, pady=10)

    def new_feature(self):
        # Implement the new feature here
        pass
```

## 6. Image Processing

Image processing is handled in `src/favicon_creator/image_processor.py`. We use the Pillow library for image manipulation.

Key functions:

- `convert_to_favicon(image_path, output_path)`: Converts an image to .ico format
- `resize_image(image, size)`: Resizes an image while maintaining aspect ratio

When adding new image processing features:

1. Write the core logic in `image_processor.py`
2. Use Pillow's built-in functions when possible
3. Handle exceptions and provide meaningful error messages
4. Write unit tests for new functions

Example of a new image processing function:

```python
from PIL import Image, ImageEnhance

def adjust_brightness(image_path, factor):
    """
    Adjust the brightness of an image.
    
    :param image_path: Path to the input image
    :param factor: Brightness adjustment factor (0.0 to 2.0)
    :return: Adjusted image object
    """
    try:
        with Image.open(image_path) as img:
            enhancer = ImageEnhance.Brightness(img)
            adjusted_img = enhancer.enhance(factor)
            return adjusted_img
    except Exception as e:
        raise ValueError(f"Error adjusting image brightness: {str(e)}")
```

## 7. Testing

We use pytest for unit testing. Test files are located in the `tests/` directory.

To run tests:

```
pytest
```

When writing tests:

1. Name test files with the prefix `test_`
2. Use descriptive test function names
3. Use pytest fixtures for setup and teardown
4. Aim for at least 80% code coverage

Example test:

```python
import pytest
from favicon_creator.image_processor import adjust_brightness

def test_adjust_brightness():
    # Setup
    test_image_path = "tests/test_images/test.png"
    
    # Test normal brightness
    result = adjust_brightness(test_image_path, 1.0)
    assert result.mode == "RGB"
    
    # Test increased brightness
    result = adjust_brightness(test_image_path, 1.5)
    assert result.mode == "RGB"
    
    # Test decreased brightness
    result = adjust_brightness(test_image_path, 0.5)
    assert result.mode == "RGB"
    
    # Test invalid factor
    with pytest.raises(ValueError):
        adjust_brightness(test_image_path, -1.0)
```

## 8. Documentation

We use Markdown for documentation. Key files:

- `README.md`: Project overview and quick start guide
- `docs/user_guide.md`: End-user documentation
- `docs/developer_guide.md`: This guide

When updating documentation:

1. Keep language clear and concise
2. Use proper Markdown formatting
3. Include code examples where appropriate
4. Update the table of contents if adding new sections

## 9. Version Control and Git Workflow

We use Git for version control. Our workflow:

1. Create a new branch for each feature or bug fix
2. Make commits with clear, descriptive messages
3. Push your branch and create a pull request
4. After review and approval, merge into the main branch

Commit message format:

```
<type>: <subject>

<body>

<footer>
```

Types: feat, fix, docs, style, refactor, test, chore

Example:

```
feat: add image brightness adjustment

- Implement adjust_brightness function in image_processor.py
- Add unit tests for adjust_brightness
- Update GUI to include brightness slider

Closes #123
```

## 10. Continuous Integration and Deployment

We use GitHub Actions for CI/CD. The workflow is defined in `.github/workflows/ci.yml`.

The CI pipeline:

1. Runs on each push and pull request
2. Sets up Python environment
3. Installs dependencies
4. Runs linting (flake8)
5. Runs tests (pytest)
6. Checks code coverage

To view CI results, check the "Actions" tab in the GitHub repository.

## 11. Contributing

We welcome contributions! To contribute:

1. Fork the repository
2. Create a new branch
3. Make your changes
4. Write or update tests
5. Update documentation
6. Create a pull request

Please review our [Code of Conduct](CODE_OF_CONDUCT.md) before contributing.

## 12. Troubleshooting

Common issues and solutions:

1. **ImportError: No module named 'favicon_creator'**
   - Ensure you've installed the package in editable mode: `pip install -e .`

2. **Tkinter not found**
   - Install Tkinter: `sudo apt-get install python3-tk` (on Ubuntu/Debian)

3. **Tests failing**
   - Ensure all dependencies are installed: `pip install -r requirements.txt`
   - Check if you're using the correct Python version

For more help, create an issue on GitHub or contact the maintainers.

---

<p align="center">
  <img src="https://github.com/burnt-exe/favicon-creator/raw/89643f237aa756df4a0b80b6fb276e81ad209c18/assets/fiiltered.png" alt="Skunkworks Projects Logo" width="100"/>
</p>

<p align="center">
  Happy coding! 🚀
</p>
