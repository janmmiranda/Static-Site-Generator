import unittest

from textnode import TextNode
from text_type_enum import TextType
from inline_markdown import split_nodes_delimiter


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

if __name__ == "__main__":
    unittest.main()
