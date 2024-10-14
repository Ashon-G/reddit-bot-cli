from setuptools import setup, find_packages
import os

# Utility function to read the README file
def read(file_name):
    with open(os.path.join(os.path.dirname(__file__), file_name), 'r', encoding='utf-8') as f:
        return f.read()

setup(
    name="reddit_bot_cli",
    version="0.0.5",
    packages=find_packages(),
    install_requires=[
        "praw",  # Your bot relies on PRAW (Python Reddit API Wrapper)
    ],
    entry_points={
        "console_scripts": [
            "reddit-bot-cli=reddit_bot.cli:main",  # The command line script
        ],
    },
    include_package_data=True,
    description="A Reddit bot that searches for keywords and posts comments.",
    long_description=read('README.md'),  # Reading the README file as long description
    long_description_content_type='text/markdown',  # Markdown format
    author="Vashon Gonzales",
    author_email="vashon@itscoop.com",
    url="https://github.com/VashonG/lead",  # Ensure this points to your repo
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',  # Ensure compatibility with Python 3.6 or higher
)
