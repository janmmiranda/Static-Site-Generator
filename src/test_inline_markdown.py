import unittest

from textnode import TextNode
from text_type_enum import TextType
from inline_markdown import *


class TestInlineMarkdown(unittest.TestCase):
    def test_split_nodes_delim_code(self):
        text_node = TextNode("This is text with a `code block` word", TextType.text.name)
        actual = split_nodes_delimiter([text_node], "`", TextType.code.name)
        expected = [
            TextNode("This is text with a ", TextType.text.name),
            TextNode("code block", TextType.code.name),
            TextNode(" word", TextType.text.name),
        ]
        print(f"actual:  {actual} \nexpected: {expected}")
        self.assertEqual(len(actual), len(expected))
        for i in range(len(expected)):
            self.assertEqual(repr(actual[i]), repr(expected[i]))
        print("============================================================")

    def test_split_nodes_delim_bold(self):
        text_node = TextNode("This is text with a *bolded* word", TextType.text.name)
        actual = split_nodes_delimiter([text_node], "*", TextType.bold.name)
        expected = [
            TextNode("This is text with a ", TextType.text.name),
            TextNode("bolded", TextType.bold.name),
            TextNode(" word", TextType.text.name),
        ]
        print(f"actual:  {actual} \nexpected: {expected}")
        self.assertEqual(len(actual), len(expected))
        for i in range(len(expected)):
            self.assertEqual(repr(actual[i]), repr(expected[i]))
        print("============================================================")

    def test_split_nodes_delim_italics_multi(self):
        text_node = TextNode("This is text with **two** words **italicized**", TextType.text.name)
        actual = split_nodes_delimiter([text_node], "**", TextType.italic.name)
        expected = [
            TextNode("This is text with ", TextType.text.name),
            TextNode("two", TextType.italic.name),
            TextNode(" words ", TextType.text.name),
            TextNode("italicized", TextType.italic.name)
        ]
        print(f"actual:  {actual} \nexpected: {expected}")
        self.assertEqual(len(actual), len(expected))
        for i in range(len(expected)):
            self.assertEqual(repr(actual[i]), repr(expected[i]))
        print("============================================================")

    def test_split_nodes_no_delim(self):
        text_node = TextNode("This is text", TextType.text.name)
        actual = split_nodes_delimiter([text_node], "**", TextType.italic.name)
        expected = [
            TextNode("This is text", TextType.text.name),

        ]
        print(f"actual:  {actual} \nexpected: {expected}")
        self.assertEqual(len(actual), len(expected))
        for i in range(len(expected)):
            self.assertEqual(repr(actual[i]), repr(expected[i]))
        print("============================================================")

    def test_extract_markdown_images(self):
        text = "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and ![another](https://i.imgur.com/dfsdkjfd.png)"
        actual = extract_markdown_images(text)
        expected = [
            ("image", "https://i.imgur.com/zjjcJKZ.png"), 
            ("another", "https://i.imgur.com/dfsdkjfd.png")
        ]
        print(f"actual:  {actual} \nexpected: {expected}")
        self.assertEqual(actual, expected)
        print("============================================================")

    def test_extract_markdown_links(self):
        text = "This is text with a [link](https://www.example.com) and [another](https://www.example.com/another)"
        actual = extract_markdown_links(text)
        expected = [
            ("link", "https://www.example.com"), 
            ("another", "https://www.example.com/another")
        ]
        print(f"actual:  {actual} \nexpected: {expected}")
        self.assertEqual(actual, expected)
        print("============================================================")

    def test_split_nodes_image(self):
        text_node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.text.name
        )
        actual = split_nodes_image([text_node])
        expected = [
            TextNode("This is text with an ", "text", None), 
            TextNode("image", "image", "https://i.imgur.com/zjjcJKZ.png"), 
            TextNode(" and another ", "text", None), 
            TextNode("second image", "image", "https://i.imgur.com/3elNhQu.png")
        ]
        print(f"actual:  {actual} \nexpected: {expected}")
        self.assertEqual(actual, expected)
        print("============================================================")

    def test_split_nodes_link(self):
        text_node = TextNode(
            "This is text with a [link](https://www.example.com) and [another](https://www.example.com/another)",
            TextType.text.name
        )
        actual = split_nodes_link([text_node])
        expected = [
            TextNode("This is text with a ", "text", None), 
            TextNode("link", "link", "https://www.example.com"), 
            TextNode(" and ", "text", None), 
            TextNode("another", "link", "https://www.example.com/another")
        ]
        print(f"actual:  {actual} \nexpected: {expected}")
        self.assertEqual(actual, expected)
        print("============================================================")

    def test_text_to_textnodes(self):
        text = "This is **text** with an *italic* word and a `code block` and an ![image](https://i.imgur.com/zjjcJKZ.png) and a [link](https://boot.dev)"
        actual = text_to_textnodes(text)
        expected = [
            TextNode("This is ", "text", None), 
            TextNode("text", "bold", None), 
            TextNode(" with an ", "text", None), 
            TextNode("italic", "italic", None), 
            TextNode(" word and a ", "text", None), 
            TextNode("code block", "code", None), 
            TextNode(" and an ", "text", None), 
            TextNode("image", "image", "https://i.imgur.com/zjjcJKZ.png"), 
            TextNode(" and a ", "text", None), 
            TextNode("link", "link", "https://boot.dev")
        ]
        print(f"actual:  {actual} \nexpected: {expected}")
        self.assertEqual(actual, expected)
        print("============================================================")

if __name__ == "__main__":
    unittest.main()
