import re

def main():
    pass

# TODO
class CSSInfo():
    def __init__(self, stylesheet_path) -> None:
        self.stylesheet_path = stylesheet_path
        with open(stylesheet_path, 'r') as file:
            self.contents = file.readlines()

    
    def get_classes(self):
        classes = [] # Create list that includes each CSS class
        for line in self.contents:
            if line.startswith("."): # Find the classes created within the stylesheet
                # Remove class indicator and opening brackets
                css_class = line.strip().lstrip(".").rstrip(" {")
                if not re.search(r"^.*(\s|:)+.*$", css_class):
                    classes.append(css_class)    

        return classes

    def get_ids(self):
        pass


    def get_media(self):
        pass

    
    def get_elements(self):
        pass

# TODO
class HTMLInfo():
    def __init__(self) -> None:
        pass


    def get_classes(self):
        pass


    def get_ids(self):
        pass


    def get_inline(self):
        pass


if __name__ == "__main__":
    main()