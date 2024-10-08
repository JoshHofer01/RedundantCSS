# StyleMapper
##### Current Version: Beta 1.0.2 [(View project on PyPi)](https://pypi.org/project/stylemapper/)

### **Contents:**
- [Description](#description)
- [Installation](#installation)
- [Usage](#usage)
- [Arguments](#keyword-arguments--choices)
- [Examples](#usages)

## **Description:**
This command line program analyzes CSS & HTML files based on the arguments you run stylemapper with. See below for usage info, and keyword argument info. StyleMapper makes tracking selectors and styles easier for web developers.

## **Installation:**
    pip install stylemapper

## **Usages:**
    stylemapper [-h / --help | -u / --usage]
    stylemapper --compare 'stylesheet_path' 'html_folder_path'
    stylemapper --getcss [choices] 'stylesheet_path'
    stylemapper --gethtml [choices] 'html_file_path' | 'html_folder_path'

<hr>

###  **Keyword Arguments & Choices:**
**'--compare':**  Compare will retrieve all class selectors from CSS stylesheet, and scan the provided HTML files to let you know which selectors are not being used in your HTML code.

**'--getcss':** Scans the stylesheet path you provide for information, which you can select with one, or more, of the required selectors.
  - classes_css: Provides table with all classes, and class count, found in stylesheet.
  - ids: Provides table with all id selectors created in stylesheet
  - media: Provides table with all media queries found in stylesheet
  - elements: Provides table will all examples of element styling found in styleshet.
  - all: Provides a table of all above information

**'--gethtml':** Scans the folder or HTML path you provide for information, which you can select with one, or more, of the required selectors.
  - classes_html: Provides table with all classes, and class count, used in HTML files.
  - ids: Provides table will all id's used in HTML files.
  - inline: Provides table with all instances of inline styling found in HTML files.
  - all: Provides a table of all above information.

**No arguments:** FEATURE COMING SOON *(This will scan your entire working directory from the root folder for all instances of CSS and HTML files, where you are able to  view information based on choices you have selected.)*



### **Path Arguments**:
  - 'stylesheet_path': Path to the CSS stylesheet to be analyzed.
    - If your styles.css sheet is within another folder, please specify this folder first, eg *static/styles.css*.
  - 'template_path_or_template_paths': Path to a folder containing HTML templates or paths to individual template files.

<hr> 

####  Examples:
  1. Analyze a single HTML template for classes and ids:
     stylemapper --gethtml classes_html ids template1.html

  2. Analyze multiple templates in a folder:
     stylemapper --gethtml all html_folder/

  3. Checking for unused CSS classes in HTML files
     stylemapper --compare styles.css html_folder/