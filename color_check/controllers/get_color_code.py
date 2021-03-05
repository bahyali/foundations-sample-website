from typing import Optional
import json


# This file should contain a function called get_color_code().
# This function should take one argument, a color name,
# and it should return one argument, the hex code of the color,
# if that color exists in our data. If it does not exist, you should
# raise and handle an error that helps both you as a developer,
# for example by logging the request and error, and the user,
# letting them know that their color doesn't exist.

class NoColorExistsError(Exception):
    pass


def get_color_code(color_name) -> Optional[str]:
    # this is where you should add your logic to check the color.
    # Open the file at data/css-color-names.json, and return the hex code
    # The file can be considered as JSON format, or as a Python dictionary.

    with open("color_check/data/css-color-names.json") as reader:
        file_content = reader.read()
        color_list = json.loads(file_content)

        if color_name in color_list:
            hex_code = color_list[color_name]
        else:
            raise NoColorExistsError
    return hex_code
