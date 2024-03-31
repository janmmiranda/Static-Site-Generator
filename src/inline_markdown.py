import re

from text_type_enum import *
from textnode import TextNode

valid_text_types = [
    TextType.bold.name,
    TextType.code.name,
    TextType.italic.name,
    TextType.text.name
]

def text_to_textnodes(text):
    text_node = TextNode(text, TextType.text.name)
    nodes_bold = split_nodes_delimiter([text_node], "**", TextType.bold.name)
    nodes_italic = split_nodes_delimiter(nodes_bold, "*", TextType.italic.name)
    nodes_code = split_nodes_delimiter(nodes_italic, "`", TextType.code.name)
    nodes_image = split_nodes_image(nodes_code)
    nodes_link = split_nodes_link(nodes_image)
    return nodes_link

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
            type = old_node.text_type
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

def split_nodes_image(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if not old_node.text_type is TextType.text.name:
            new_nodes.append(old_node)
            continue
        text = old_node.text
        images = extract_markdown_images(text)
        if len(images) == 0:
            new_nodes.append(old_node)
            continue
        for image in images:
            sections = text.split(f"![{image[0]}]({image[1]})", 1)
            if len(sections) != 2:
                raise ValueError("Invalid markdown, image not closed")
            if sections[0] != "":
                new_nodes.append(TextNode(sections[0], TextType.text.name))
            new_nodes.append(
                TextNode(image[0], TextType.image.name, image[1])
            )
            text = sections[1]
        if text != "":
            new_nodes.append(TextNode(text, TextType.text.name))
    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if not old_node.text_type is TextType.text.name:
            new_nodes.append(old_node)
            continue
        text = old_node.text
        links = extract_markdown_links(text)
        if len(links) == 0:
            new_nodes.append(old_node)
            continue
        for link in links:
            sections = text.split(f"[{link[0]}]({link[1]})", 1)
            if len(sections) != 2:
                raise ValueError("Invalid markdown, link not closed")
            if sections[0] != "":
                new_nodes.append(TextNode(sections[0], TextType.text.name))
            new_nodes.append(
                TextNode(link[0], TextType.link.name, link[1])
            )
            text = sections[1]
        if text != "":
            new_nodes.append(TextNode(text, TextType.text.name))
    return new_nodes