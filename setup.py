from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="favicon-creator",
    version="0.1.0",
    author="Skunkworks Projects",
    author_email="support@skunkworksprojects.com",
    description="A GUI application to create favicons from various image formats",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/burnt-exe/favicon-creator",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Multimedia :: Graphics :: Graphics Conversion",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
    install_requires=[
        "Pillow>=9.5.0",
        "ttkthemes>=3.2.2",
    ],
    entry_points={
        "console_scripts": [
            "favicon-creator=favicon_creator.main:main",
        ],
    },
)
