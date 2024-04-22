import re

def main():
    classes = get_css_classes(stylesheet="test files/styles.css")
    print(classes)

def get_css_classes(stylesheet):
    with open(stylesheet, 'r') as file:
        content = file.readlines() # Read the contents of CSS file

    classes = []
    for line in content:
        if line.startswith("."):
            class_line = line.strip()
            css_class = class_line.lstrip(".").rstrip(" {")
            if not re.search(r"^.*(\s|:)+.*$", css_class):
                classes.append(css_class)

    return classes


def html_classes(templates):
    pass


if __name__ == "__main__":
    main()