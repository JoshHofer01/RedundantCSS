import pytest
from redundantcss import redundantcss
from pathlib import Path

# Global variables for file paths
# Will be used in many tests

# USES PYTEST
# set paths as global variables
TEMPLATE_PATH = "tests/template1.html"  # Exact path to single html file
MULTI_PATH = ["tests/template1.html", "tests/templates/_layout.html"]  # Paths to multiple HTML files
TEMPLATES_FOLDER_PATH = "tests/templates"  # Path to folder with multiple files, ONLY html files
STYLESHEET_PATH = "tests/styles.css"  # Exact path to stylesheet

# validate_args.py function check_folder_contents(path) uses
# Path object from pathlib library. Iterates over each .html
# file within directory.
FOLDER_WITH_HTML = Path("tests/mixed_with_html")  # Folder with multiple file types, NOT including HTML files
FOLDER_WITHOUT_HTML = Path("tests/mixed_without_html")  # Folder with multiple file types, NOT including HTML files

def main():
    test_single_template_files()
    test_parses_templates_folder()
    test_parses_stylesheet()
    test_class_comparison()


# Tests for redundantcss.py
# --
# Checks for single or multiple '.html' files passed as arguments.
def test_single_template_files():
    assert redundantcss.get_html_classes(TEMPLATE_PATH) == {
        'bg-container', 'green-text', 'protest'
        }
    
    assert redundantcss.get_html_classes(MULTI_PATH) == {
        'bg-container', 'green-text', 'protest', 'page-container'
        }


# Make sure a folder name passed as argument to function parses correctly and
# each '.html' file in the folder is read.
def test_parses_templates_folder():
    assert redundantcss.get_html_classes(TEMPLATES_FOLDER_PATH) == {
        'bg-container', 'green-text', 'protest', 'page-container'
        }


# Ensure the function is returning all of the classes created
# in the 'styles.css' or stylesheet given to 'get_css_classes()'.
def test_parses_stylesheet():
    assert redundantcss.get_css_classes(STYLESHEET_PATH) == ['page-container', 'bg-container', 'title-text', 'protest', 'unused-class']


def test_class_comparison():
    css_classes = ['page-container', 'bg-container', 'title-text', 'protest', 'unused-class']
    html_classes = ['page-container', 'bg-container', 'title-text', 'protest']
    assert redundantcss.compare_classes(css_classes, html_classes) == ["unused-class"]


# Create tests for validateArgs.py
# Tests for validate_args.py
# --
# Tests function used within get_html_classes().
def test_parse_classes():
    # This function can only accept 1 html sheet at a time.
    # Error handling is done by parent function
    # Error handling being added to this function at a later stage
    with open(TEMPLATE_PATH, 'r') as html_sheet:
        assert redundantcss.parse_classes(html_sheet) == {
        'bg-container', 'green-text', 'protest'
        }


def test_no_html_folder():
    assert redundantcss.check_folder_contents(FOLDER_WITHOUT_HTML) == False


def test_mixed_folder():
    assert redundantcss.check_folder_contents(FOLDER_WITH_HTML) == True


if __name__ == "__main__":
    main()