import pathlib
from setuptools import setup, find_packages

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text(encoding='utf-8')

# This call to setup() does all the work
setup(
    name="filet",
    version="1.8.0",
    description="CLI tool for the filetree planters",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/gitwikc/filet",
    author="Sattwik Sahu",
    author_email="sahusattwik@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    packages=find_packages(exclude=('__src',)),
    include_package_data=True,
    install_requires=['colorama'],
    entry_points={
        "console_scripts": [
            "filet=src.__main__:main",
        ]
    },
)