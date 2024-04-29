from redundantcss.redundantcss import get_html_classes, get_css_classes, compare_classes
from redundantcss.validateArgs import parse_classes, check_folder_contents


# Global variables for file paths
# Will be used in many tests

# Exact path to single html file
TEMPLATE_PATH = "template1.html"

# Path to folder with multiple files, ONLY html files
TEMPLATE_FOLDER = "templates/"

# Folder with multiple file types including HTML and CSS
MIXED_FOLDER = "mixed_files/"

# Exact path to stylesheet
STYLESHEET = "styles.css"

# USES PYTEST
def main():
    pass

# Tests for redundantcss.py
# --
# Checks single '.html' file
def test_single_template_file():
    with open(TEMPLATE_PATH, 'r') as file
    assert get_html_classes(file) == ['center-title', 'song-dropdown', '


# Checks multiple '.html' files passed as argument to 'get_html_classes()'
def test_multi_template_files():
    pass


# Make sure a folder name passed as argument to function parses correctly and
# each '.html' file in the folder is read.
def test_parses_templates_folder():
    pass


# Ensure the function is returning all of the classes created
# in the 'styles.css' or stylesheet given to 'get_css_classes()'.
def test_parses_stylesheet():
    pass

# Create tests for validatArgs.py