from block_type_enum import *
from htmlnode import *
from textnode import text_node_to_html_node
from inline_markdown import text_to_textnodes
def markdown_to_blocks(markdown):
    lines = markdown.split("\n\n")
    res = []
    for line in lines:
        if line == "":
            continue
        temp = line.strip()
        res.append(temp)
    return res

def block_to_block_type(block):
    lines = block.split("\n")
    if (
        block.startswith("# ") or
        block.startswith("## ") or
        block.startswith("### ") or
        block.startswith("#### ") or
        block.startswith("##### ") or
        block.startswith("###### ") 
    ):
        return BlockType.HEADING.value
    if (
        len(lines) > 1 and
        lines[0].startswith("```") and
        lines[-1].startswith("```")
    ):
        return BlockType.CODE.value
    if block.startswith(">"):
        return BlockType.QUOTE.value
    if block.startswith("* "):
        for line in lines:
            if not line.startswith("* "):
                return BlockType.PARAGRAPH.value
        return BlockType.UNORDERED_LIST.value
    if block.startswith("- "):
        for line in lines:
            if not line.startswith("- "):
                return BlockType.PARAGRAPH.value
        return BlockType.UNORDERED_LIST.value
    if block.startswith("1. "):
        count = 1
        for line in lines:
            if not line.startswith(f"{count}. "):
                return BlockType.PARAGRAPH.value
            count += 1
        return BlockType.ORDERED_LIST.value
    return BlockType.PARAGRAPH.value

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    child_nodes = []
    for block in blocks:
        block_type = block_to_block_type(block)
        if block_type == BlockType.CODE.value:
            child_nodes.append(create_code_node(block))
        elif block_type == BlockType.HEADING.value:
            child_nodes.append(create_heading_node(block))
        elif block_type == BlockType.ORDERED_LIST.value:
            child_nodes.append(create_ol_node(block))
        elif block_type == BlockType.QUOTE.value:
            child_nodes.append(create_quote_node(block))
        elif block_type == BlockType.UNORDERED_LIST.value:
            child_nodes.append(create_ul_node(block))
        else:
            child_nodes.append(create_paragraph_node(block))
    return ParentNode("div", child_nodes)

def create_quote_node(block):
    lines = block.split("\n")
    new_lines = []
    for line in lines:
        if not line.startswith(">"):
            raise ValueError("Invalid quote block")
        new_lines.append(line.lstrip(">").strip())
    content = " ".join(new_lines)
    children = text_to_child_node(content)
    return ParentNode("blockquote", children)

def create_ul_node(block):
    items = []
    lines = block.split("\n")
    for line in lines:
        text = line[2:]
        children = text_to_child_node(text)
        items.append(ParentNode("li", children))
    return ParentNode("ul", items)

def create_ol_node(block):
    items = []
    lines = block.split("\n")
    for line in lines:
        text = line[3:]
        children = text_to_child_node(text)
        items.append(ParentNode("li", children))
    return ParentNode("ol", items)

def create_code_node(block):
    if not block.startswith("```") or not block.endswith("```"):
        raise ValueError("Invalid code block")
    text = block[4:-3]
    children = text_to_textnodes(text)
    code = ParentNode("code", children)
    return ParentNode("pre", [code])

def create_heading_node(block):
    tag = ""
    value = block
    if block.startswith("# "):
        tag = "h1"
        value = block.split("# ")[1]
    elif block.startswith("## "):
        tag = "h2"
        value = block.split("## ")[1]
    elif block.startswith("### "):
        tag = "h3"
        value = block.split("### ")[1]
    elif block.startswith("#### "):
        tag = "h4"
        value = block.split("#### ")[1]
    elif block.startswith("##### "):
        tag = "h5"
        value = block.split("##### ")[1]
    else:
        tag = "h6"
        value = block.split("###### ")[1]
    children = text_to_child_node(value)
    return ParentNode(tag, children)

def create_paragraph_node(block):
    lines = block.split("\n")
    paragraph = " ".join(lines)
    children = text_to_child_node(paragraph)
    return ParentNode("p", children)

def text_to_child_node(text):
    text_nodes = text_to_textnodes(text)
    children = []
    for text_node in text_nodes:
        html_node = text_node_to_html_node(text_node)
        children.append(html_node)
    return children
