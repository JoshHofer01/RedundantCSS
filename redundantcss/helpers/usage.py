usage = """
USAGES: redundantcss [-h / --help | -u / --usage]
        redundantcss --compare 'stylesheet_path' 'html_folder_path'
        redundantcss --getcss [choices] 'stylesheet_path'
        redundantcss --gethtml [choices] 'html_file_path' | 'html_folder_path'
        To see argument choices, please run 'redundantcss -h'

Keyword arguments:
    No argument: FEATURE COMING SOON (This will scan your entire working directory from the root folder
                 for all instances of CSS and HTML files, where you are able to 
                 view information based on choices you have selected.)
    '--compare':  Compare will retrieve all class selectors from CSS stylesheet,
                  and scan the provided HTML files to let you know which selectors
                  are not being used in your HTML code.
    '--getcss': Scans the stylesheet path you provide for information, which 
                you can select with one, or more, of the required selectors.
    '--gethtml': Scans the folder or HTML path you provide for information, which 
                 you can select with one, or more, of the required selectors.

Arguments:
    - 'stylesheet_path': Path to the CSS stylesheet to be analyzed.
    - 'template_path/template_paths/folder_path>': Path to a folder containing HTML templates or paths to individual template files."""