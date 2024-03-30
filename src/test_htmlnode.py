import unittest

from htmlnode import *


class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        node = HTMLNode("a", "link", None, {"href": "https://www.google.com", "target": "_blank"})
        prop_converted = node.props_to_html()
        self.assertEqual(prop_converted, " href=\"https://www.google.com\" target=\"_blank\"")

    def test_raise_notImplementedError(self):
        node = HTMLNode()
        try:
            node.to_html()
        except NotImplementedError as e:
            self.assertEqual("to_html method not implemented", str(e))

    def test_leafnode_to_html_p(self):
        node = LeafNode("This is a paragraph of text.", "p")
        value_converted = node.to_html()
        self.assertEqual(value_converted, "<p>This is a paragraph of text.</p>")

    def test_leafnode_to_html_a(self):
        node = LeafNode("Click me!", "a", None, {"href": "https://www.google.com"})
        value_converted = node.to_html()
        self.assertEqual(value_converted, "<a href=\"https://www.google.com\">Click me!</a>")

    def test_leafnode_to_html(self):
        node = LeafNode("This is a paragraph of text.")
        value_converted = node.to_html()
        self.assertEqual(value_converted, "This is a paragraph of text.")

if __name__ == "__main__":
    unittest.main()
