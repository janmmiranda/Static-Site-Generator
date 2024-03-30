import re

from text_type_enum import *
from textnode import TextNode

valid_text_types = [
    TextType.bold.name,
    TextType.code.name,
    TextType.italic.name,
    TextType.text.name
]

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for old_node in old_nodes:
        if not text_type in valid_text_types:
            new_nodes.append(old_node)
            continue
        split_nodes = []
        texts = old_node.text.split(delimiter)
        if len(texts) % 2 == 0:
            return ValueError(f"{delimiter} does not close properly")
        for i in range(len(texts)):
            if texts[i] == "":
                continue
            type = TextType.text.name
            if not i % 2 == 0:
                type = text_type
            split_nodes.append(TextNode(texts[i], type))
        new_nodes.extend(split_nodes)
    return new_nodes

def extract_markdown_images(text):
    matches = re.findall(r"!\[(.*?)\]\((.*?)\)", text)
    return matches

def extract_markdown_links(text):
    matches = re.findall(r"\[(.*?)\]\((.*?)\)", text)
    return matches