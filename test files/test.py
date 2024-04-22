import re

# Open the CSS file
with open('styles.css', 'r') as file:
    # Read the contents of the file
    content = file.readlines()

# Now you have the CSS content stored in the variable css_content
classes = []
for line in content:
    if line.startswith("."):
        class_line = line.strip()
        css_class = class_line.lstrip(".").rstrip(" {")
        if not re.search(r"^.*(\s|:)+.*$", css_class):
            print(css_class)

"""# Open the HTML file
with open('index.html', 'r') as file:
    # Read the contents of the file
    html_content = file.read()

# Now you have the HTML content stored in the variable html_content
print(html_content)"""

