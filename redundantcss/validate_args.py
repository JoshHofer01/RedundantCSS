from bs4 import BeautifulSoup
import argparse
import os
from pathlib import Path


# PROBABLY REWRITE
def parse_classes(html_sheet):
    classes = set()
    content = html_sheet.read()
    soup = BeautifulSoup(content, 'html.parser')
    elements_with_class = soup.find_all(class_=True)

    for element in elements_with_class:
        classes.update(element.get("class"))
  
    return classes


# PROBABLY REWRITE
def check_folder_contents(path):
    html_count = 0
    other_file_count = 0
    for file_path in path.iterdir():
        if str(file_path).endswith(".html"):
            html_count += 1
        else:
            other_file_count += 1

    if other_file_count >= 0 and html_count == 0:
        return False
    elif html_count > 0:
        return True


class GetHTMLPath(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        choices = ["classes_html", "inline", "ids"]
        needed_choices = set()
        other_choices = set()

        if values:
            for value in values:
                if value in choices:
                    needed_choices.add(value)
                else:
                    other_choices.add(value)
        
        if not needed_choices:
            parser.error(f"At least 1 choice from {choices} is required.")

        setattr(namespace, self.dest, needed_choices)
        setattr(namespace, "other_choices", other_choices)


class GetCSSPath(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        choices = ["classes_css", "ids", "media", "element"]
        needed_choices = set()
        other_choices = set()

        if values:
            for value in values:
                if value in choices:
                    needed_choices.add(value)
                else:
                    other_choices.add(value)
        
        if not needed_choices:
            parser.error(f"At least 1 choice from {choices} is required.")

        setattr(namespace, self.dest, needed_choices)
        setattr(namespace, "other_choices", other_choices)


def create_flags():
    parser = argparse.ArgumentParser(
        prog = "redundantcss",
        description = "This script analyzes a stylesheets and templates, providing information regarding classes & styling used.",
        formatter_class=argparse.RawTextHelpFormatter,
    )
    parser.usage = """Usage: redundantcss [-h | -u] [[--getcss [choices]] | [--gethtml [choices]] <stylesheet> <template_folder OR template_paths>
Use 'redundantcss -u | --usage' for detailed info info."""

    
    group = parser.add_mutually_exclusive_group()

    group.add_argument('-u', '--usage',
                       help="Details all ways to use programm, including flag usage.",
                       action='store_true')
    
    group.add_argument('--getcss',
                       action=GetCSSPath,
                       nargs='+',
                       metavar="[choice]",
                       help="""CHOICES: ["classes_css", "ids", "media", "element"]
--------------------------------------------
You MUST include at least one choice from CHOICES after --getcss. 
You may also pass '.css' files as extra arguments if you want to 
only scan specific files. If no path or folder is passed an extra 
argument, redundantcss will scan entire directory for all instances 
of '.css' files to read and return info based on your choice.
--------------------------------------------
classes_css: gets all classes created within stylesheet
ids: gets name of all ids created within stylesheet
media: gets all @media querise created within stylesheet
element: gets all instances of styling created on specific
elements.\n
""")

    
    group.add_argument('--gethtml',
                       action=GetHTMLPath,
                       metavar="[choice]",
                       nargs="+",
                       help="""CHOICES: ["classes_html", "inline", "ids"]
--------------------------------------------
You MUST include at least one choice from CHOICES after --gethtml. 
You may also pass '.html' files as extra arguments if you want to 
only scan specific files. If no path or folder is passed an extra 
argument, redundantcss will scan entire directory for all instances 
of '.html' files to read and return info based on your choice.
--------------------------------------------
classes_html: gets all classes used within html files
inline: gets instances of all inline styling used, along with 
line number and file name.
ids: gets name of all ids used within html files.\n
""")
    
    return parser


# PROBABLY REWRITE
def validate_flag(user_flag, flags):
    current_flag = ""  # assert blank flag variable
    for flag in flags:
        if user_flag == flag['short_flag'] or user_flag == flag['long_flag']:
            if not current_flag:  # only continue if a flag has not already been filled
                current_flag = flag['long_flag']
            return False  # if more than one flag has been used
        return False  # if flag does not match an accepted flag
    return current_flag  # if passes all validation


def is_css_file(file_path: Path):
    if not file_path.exists():
        return False
    
    try:
        if not str(file_path).endswith(".css"):
            return False
    except TypeError:
        return False
    
    return True


def is_html_file(file_path):
    if not os.path.exists(file_path):
        return False
    
    try:
        if not str(file_path).endswith(".html"):
            return False
    except TypeError:
        return False
    
    return True
