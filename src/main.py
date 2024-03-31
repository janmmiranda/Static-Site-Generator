from textnode import *
from htmlnode import *
from text_type_enum import *
from inline_markdown import *
from block_markdown import *
from block_type_enum import *
from static_helper import copy_dir

def main():
#     md = """
# # this is an h1

# this is **paragraph** text

# ## this is an h2
# """
#     html = markdown_to_html_node(md)
#     print(html.to_html())
    source = "static/"
    target = "public/"
    copy_dir(source, target)
main()