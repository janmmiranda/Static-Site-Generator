from htmlnode import LeafNode
from text_type_enum import *

class TextNode():
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, text_node):
        if (
            self.text == text_node.text and
            self.text_type == text_node.text_type and
            self.url == text_node.url
        ):
            return True
        else:
            return False
        
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type}, {self.url})"
    
def text_node_to_html_node(text_node):
    tag = convert_to_tag(text_node.text_type)
    value = None
    props = None
    if text_node.text_type == TextType.link.name:
        props = create_props(href=text_node.url)
        value = text_node.text
    elif text_node.text_type == TextType.image.name:
        props = create_props(src=text_node.url, alt=text_node.text)
    else:
        value = text_node.text
    return LeafNode(tag, value, props)

def create_props(**kwargs):
    props = {}
    for key, value in kwargs.items():
        props[key] = value
    return props