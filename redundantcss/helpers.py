usage = """USAGE: python redundantcss.py <stylesheet_path> <template_path_or_template_paths>

Description:
  This script analyzes a stylesheet and identifies redundant CSS rules not used by the templates provided.

Arguments:
  - 'stylesheet_path': Path to the CSS stylesheet to be analyzed.
  - 'template_path_or_template_paths': Path to a folder containing HTML templates or paths to individual template files.

Examples:
  1. Analyze a single template:
     python redundantcss.py 'styles.css' 'template.html'

  2. Analyze multiple templates in a folder:
     python redundantcss.py 'styles.css' 'templates/'

  3. Analyze multiple templates provided as separate arguments:
     python redundantcss.py 'styles.css' 'template1.html' 'template2.html' 'template3.html'"""


help_string = ""
