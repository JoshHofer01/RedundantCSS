# StyleMapper changelog
### Wednesday 18th September 2024
Beta Version 1.0.2 - "Small Changes"
1. Removed small bug where folder paths would print onto the terminal during '--compare'
2. Updated documentation accordingly with first full release onto PyPi.

Beta Version 1.0.0 - "StyleMapper"

1. Renamed program to StyleMapper to better align with what the program does, and will do in the future
2. Fixed recursive function in `validate_paths.py` to return correct list of all HTML files in a folder.

### Tuesday 17th September 2024
Pre-release Version 0.0.4 - "Refactoring RedundantCSS"

1. Major refactor of code into dedicated functions and classes
    - Main body of `redundantcss.py` is now 1 if/elif/else statement
    - Created multiple new modules with dedicated functions for increased modulation and flexibility across programm
        - Created `beautify.py`, `compare.py`, `read_args.py`, `set_argparse.py`, `usage.py`, and `validate_paths.py`
        - Deleted `read_paths.py`, `validate_args.py`, and `helpers.py`
        - Began using 'tabulate' package to present output in terminal.
    - Created HTMLInfo, CSSInfo, and Compare
2. Added reliability on 'argparse' library for more powerful command line arguments
    - Added path verification and file validation into custom classes created in argparse
    - Removed barebones argument parsing that used sys.argv to parse arguments.
    - Created '--getcss' with GetCSSInfo class
        - Program ignores classes with additional selectors, pseudo-elements, and psuedo-classes
    - Created '--gethtml' with GetHTMLInfo class 
    - Created '--compare' with CheckComparisonPaths class
        - Compare only accepts 1 stylesheet path, and 1 folder path containing HTML files
3. Re-created tests for three major files within helpers/ that `redundantcss.py `relies on. `compare.py`, `read_args.py`, and `validate_paths.py`.
4. Added more notes, documentation, and docstrings into program.
5. Updated `README.md`
