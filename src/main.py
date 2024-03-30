from textnode import TextNode
from htmlnode import *
from text_type_enum import *
from inline_markdown import *

def main():
    test = TextNode("This is a text node link", "link", "https://www.boot.dev")
    print(repr(test))
    html = test.text_node_to_html_node(test)
    print(repr(html))
    text = "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and ![another](https://i.imgur.com/dfsdkjfd.png)"
    print(extract_markdown_images(text))

    text = "This is text with a [link](https://www.example.com) and [another](https://www.example.com/another)"
    print(extract_markdown_links(text))


main()