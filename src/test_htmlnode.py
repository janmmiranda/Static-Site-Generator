import unittest

from htmlnode import *

# tag, value, children, props
class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        node = HTMLNode("a", "link", None, {"href": "https://www.google.com", "target": "_blank"})
        actual = node.props_to_html()
        expected = " href=\"https://www.google.com\" target=\"_blank\""
        print(f"actual:  {actual} \nexpected: {expected}")
        self.assertEqual(actual, expected)
        print("============================================================")

    def test_raise_notImplementedError(self):
        node = HTMLNode()
        try:
            node.to_html()
        except NotImplementedError as e:
            expected = "to_html method not implemented"
            actual = str(e)
            print(f"actual:  {actual} \nexpected: {expected}")
            self.assertEqual(expected, actual)
            print("============================================================")

    def test_leafnode_to_html_p(self):
        node = LeafNode("p", "This is a paragraph of text.")
        actual = node.to_html()
        expected = "<p>This is a paragraph of text.</p>"
        print(f"actual:  {actual} \nexpected: {expected}")
        self.assertEqual(actual, expected)
        print("============================================================")


    def test_leafnode_to_html_a(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        actual = node.to_html()
        expected = "<a href=\"https://www.google.com\">Click me!</a>"
        print(f"actual:  {actual} \nexpected: {expected}")
        self.assertEqual(actual, expected)
        print("============================================================")

    def test_leafnode_to_html(self):
        node = LeafNode(None, "This is a paragraph of text.")
        actual = node.to_html()
        expected = "This is a paragraph of text."
        print(f"actual:  {actual} \nexpected: {expected}")
        self.assertEqual(actual, expected)
        print("============================================================")

    def test_to_html_with_child(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        actual = parent_node.to_html()
        expected = "<div><span>child</span></div>"
        print(f"actual:  {actual} \nexpected: {expected}")
        self.assertEqual(actual, expected)
        print("============================================================")

    def test_to_html_with_granchild(self):
        granchild_node = LeafNode("span", "granchild")
        child_node = ParentNode("div", [granchild_node])
        parent_node = ParentNode("div", [child_node])
        actual = parent_node.to_html()
        expected = "<div><div><span>granchild</span></div></div>"
        print(f"actual: {actual} \nexpected: {expected}")
        self.assertEqual(actual, expected)
        print("============================================================")

    def test_to_html_with_many_childs(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text")
            ]
        )
        actual = node.to_html()
        expected = "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>"
        print(f"actual: {actual} \nexpected: {expected}")
        self.assertEqual(actual, expected)
        print("============================================================")

if __name__ == "__main__":
    unittest.main()
