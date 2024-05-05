import re
import sys
from pathlib import Path
import os
import argparse

from redundantcss.validate_args import parse_classes, check_folder_contents, create_flags, is_css_file, is_html_file
from redundantcss.read_paths import CSSInfo, HTMLInfo
from redundantcss.helpers import usage


def main():
    arg_count = len(sys.argv)
    parser = create_flags()
    args: argparse.Namespace = parser.parse_args()
    # TODO: Rewrite ie/elif/else statement to include custom values from argparse
    # TODO: Remove reliability on sys for arg parsing
    # TODO: Refactor EVERYTHING into functions, either in read_paths or validate_args
    # TODO: Vet .other_choices to ensure they are valid filetypes
    # * Clean up code in this file
    # * File should ONLY contain if/elif/else statement

    # TODO
    if args.getcss:  # checks for --getcss flag
        # Assert dictionary that maps all --getcss choices to respective functions
        css_arg_functions = {
            "ids": CSSInfo.get_ids,
            "classes_css": CSSInfo.get_classes,
            "media": CSSInfo.get_media,
            "element": CSSInfo.get_elements}

        if args.other_choices:  # If user specifies path(s) to read
            stylesheet_paths = []

            for choice in args.other_choices:
                # Validate that each choice is a '.css' file that exists
                if not is_css_file(choice):
                    print(f"{choice} is an invalid stylesheet path. Use 'redundantcss [-u or -h]' for help.")
                    sys.exit()
                else:
                    stylesheet_paths.append(choice)

            if not check_file_extensions():
                print("Your files are not all CSS files. Use 'redundantcss [-u or -h]' for help.")
        
        else:   # TODO: Logic to look through entire directory for '.css' files
           pass
         
        cssinfo = CSSInfo(stylesheet_paths)  # Create CSSInfo object if all conditions are valid/met.

        for arg in args.getcss:  # loop to run the the function based on the users request
            try:
                result = css_arg_functions[arg]()
            except:
                print(f"ERROR: No function defined for argument {arg}")
            
            # TODO: Print result nicely
            # Amount of items
        
    elif args.gethtml:  # checks for --gethtml flag
        html_arg_functions = {
            "ids": HTMLInfo.get_ids,
            "classes_html": HTMLInfo.get_classes,
            "inline": HTMLInfo.get_inline}
        # Duplicate CSS info checks but convert to checks for HTML using HTML funcs
        pass

    else:  # if programm is run without arguments passed
        if len(sys.argv) == 1:
            # Create func for scanning directory for HTML and CSS files
            pass
        else:
            print("Incorrect usage. Use 'redundantcss [-u or -h]' for help.")
            sys.exit()

        


    if arg_count == 1:
        print("This feature is not currently implemented")
        sys.exit()

    elif arg_count == 2:
        ...

    elif arg_count == 3: 
        # Check if filepath for 2nd arg exists
        if not os.path.exists(sys.argv[2]):
            print("Your folder or filepath does not exist, run 'redundantcss' on its own for usage.")
            sys.exit()
        template_info = sys.argv[2]

    # Multiple args accepts multiple html files instead of folder path. 
    elif arg_count > 3:
        template_info = sys.argv[2:]
        # Check each filepath for validity before continuing
        for file in template_info:
            if not file.endswith(".html"):
                print(f"Error with '{file}', please end filename with '.html' and ensure it exists.")
                sys.exit()
            if not os.path.exists(file):
                print(f"'{file}' does not exist, please ensure this is the correct path and try again.")
                sys.exit()

    if not os.path.exists(sys.argv[1]):
        print("Stylesheet path does not exist, run 'redundantcss' on its own for usage.")
        sys.exit()
    stylesheet_path = sys.argv[1]

    css_classes: list = get_css_classes(stylesheet_path)
    html_classes: set = get_html_classes(template_info)
    unused_classes: list = compare_classes(css_classes, html_classes)

    print(f"You have {len(unused_classes)} unused classes out of {len(css_classes)}.")
    print(f"All unused CSS classes:")
    for item in unused_classes:
        print(item)


def get_css_classes(stylesheet: str):
    with open(stylesheet, 'r') as file:
        content = file.readlines()  # Read the contents of CSS file

    classes = []  # Create list that includes each CSS class
    for line in content:
        if line.startswith("."): # Find the classes created within the stylesheet
            # Remove class indicator and opening brackets
            css_class = line.strip().lstrip(".").rstrip(" {")
            if not re.search(r"^.*(\s|:)+.*$", css_class):
                classes.append(css_class)

    return classes


def get_html_classes(path):
    classes_used = set()
    # If path passed is template file.
    if path.endswith(".html"):
        with open(path, 'r') as html_sheet:
            classes_used.update(parse_classes(html_sheet))
    # If folder path is passed as path.
    else:
        folder_path = Path(path)
        if not check_folder_contents(folder_path):
            print("There are no HTML files in this folder")
            sys.exit()

        for file_path in folder_path.iterdir():
            if file_path.is_file() and str(file_path).endswith(".html"):
                with open(file_path, 'r') as html_sheet:
                    classes_used.update(parse_classes(html_sheet)) 

    return classes_used 


def compare_classes(css_classes: list, html_classes: list):
    unused_classes = []
    for item in css_classes:
        if item not in html_classes:
            unused_classes.append(item)

    return unused_classes


if __name__ == "__main__":
    main()
