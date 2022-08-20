"""
Parse my own markdown flavor. Glue script, just glues this together. Classes in other files in pwd.
"""

def get_parsed_file_contents(path_to_file: str):
    """
    Glue function
    """

    with open(path_to_file, encoding='utf-8') as file:
        lexed: list = file.readlines()
