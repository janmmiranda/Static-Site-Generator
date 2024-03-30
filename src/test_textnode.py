import unittest

from textnode import TextNode
from htmlnode import LeafNode
from text_type_enum import TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.bold.name)
        node2 = TextNode("This is a text node", TextType.bold.name)
        self.assertEqual(node, node2)

    def test_no_eq(self):
        node = TextNode("This is a text node", TextType.italic.name)
        node2 = TextNode("This is a text node", TextType.bold.name)
        self.assertNotEqual(node, node2)

    def test_eq_url(self):
        node = TextNode("This is a text node", TextType.link.name, "www.test.com")
        node2 = TextNode("This is a text node", TextType.link.name, "www.test.com")
        self.assertEqual(node, node2)

    def test_convert_to_html_text(self):
        text_node = TextNode("Text", TextType.text.name)
        html_node = text_node.text_node_to_html_node(text_node)
        leaf_node = LeafNode(None, "Text")
        self.assertEqual(repr(html_node), repr(leaf_node))

    def test_convert_to_html_link(self):
        text_node = TextNode("link", TextType.link.name, "www.link.com")
        html_node = text_node.text_node_to_html_node(text_node)
        leaf_node = LeafNode("a", "link",  {"href": "www.link.com"})
        self.assertEqual(repr(html_node), repr(leaf_node))

if __name__ == "__main__":
    unittest.main()
