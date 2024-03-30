from enum import Enum

class TextType(Enum):
    text = 1
    bold = 2
    italic = 3
    code = 4
    link = 5
    image = 6

def convert_to_tag(type):
    if type == TextType.text.name:
        return None
    if type == TextType.bold.name:
        return "b"
    if type == TextType.italic.name:
        return "i"
    if type == TextType.code.name:
        return "code"
    if type == TextType.link.name:
        return "a"
    if type == TextType.image.name:
        return "img"
    raise ValueError("Unknown type")