import unittest

from block_markdown import *

class TestBlockMarkdown(unittest.TestCase):
    def test_markdown_to_blocks(self):
        text = """
This is **bolded** paragraph

This is another paragraph with *italic* text and `code` here
This is the same paragraph on a new line

* This is a list
* with items
"""
        actual = markdown_to_blocks(text)
        expected = [
            'This is **bolded** paragraph', 
            'This is another paragraph with *italic* text and `code` here\nThis is the same paragraph on a new line', 
            '* This is a list\n* with items'
        ]
        print(f"actual:  {actual} \nexpected: {expected}")
        self.assertEqual(actual, expected)
        print("============================================================")

    def test_block_to_block_paragraph(self):
        text = "This is **bolded** paragraph"
        actual = block_to_block_type(text)
        expected = BlockType.PARAGRAPH.value
        print(f"actual:  {actual} \nexpected: {expected}")
        self.assertEqual(actual, expected)
        print("============================================================")

    def test_block_to_block_ul(self):
        text = "* This is a list\n* with items"
        actual = block_to_block_type(text)
        expected = BlockType.UNORDERED_LIST.value
        print(f"actual:  {actual} \nexpected: {expected}")
        self.assertEqual(actual, expected)
        print("============================================================")

    def test_block_to_block_ol(self):
        text = "1. This is a list\n2. with items"
        actual = block_to_block_type(text)
        expected = BlockType.ORDERED_LIST.value
        print(f"actual:  {actual} \nexpected: {expected}")
        print("============================================================")
        self.assertEqual(actual, expected)

    def test_block_to_block_heading5(self):
        text = "##### this is a heading 5"
        actual = block_to_block_type(text)
        expected = BlockType.HEADING.value
        print(f"actual:  {actual} \nexpected: {expected}")
        self.assertEqual(actual, expected)
        print("============================================================")

    def test_markdown_to_html_list(self):
        markdown = """
- This is a list
- with items
- and *more* items

1. This is an `ordered` list
2. with items
3. and more items

"""
        node = markdown_to_html_node(markdown)
        actual = node.to_html()
        expected = "<div><ul><li>This is a list</li><li>with items</li><li>and <i>more</i> items</li></ul><ol><li>This is an <code>ordered</code> list</li><li>with items</li><li>and more items</li></ol></div>"
        print(f"actual:  {actual} \nexpected: {expected}")
        print("============================================================")
        self.assertEqual(actual, expected)

    def test_markdown_to_html_headings(self):
        markdown = """
# this is an h1

this is **paragraph** text

## this is an h2
"""
        node = markdown_to_html_node(markdown)
        actual = node.to_html()
        expected = "<div><h1>this is an h1</h1><p>this is <b>paragraph</b> text</p><h2>this is an h2</h2></div>"
        print(f"actual:  {actual} \nexpected: {expected}")
        print("============================================================")
        self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()