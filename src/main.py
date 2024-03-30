from textnode import TextNode
from htmlnode import *
from text_type_enum import *

def main():
    test = TextNode("This is a text node link", "link", "https://www.boot.dev")
    print(repr(test))
    html = test.text_node_to_html_node(test)
    print(repr(html))

main()