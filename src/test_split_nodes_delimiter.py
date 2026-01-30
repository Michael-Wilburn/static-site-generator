import unittest

from textnode import TextNode, TextType
from split_nodes_delimeter import split_nodes_delimiter


class TestSplitNodesDelimiter(unittest.TestCase):
    def test_code_delimiter(self):
        node = TextNode(
            "This is text with a `code block` word",
            TextType.TEXT
        )
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)

        self.assertEqual(new_nodes, [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" word", TextType.TEXT),
        ])

    def test_bold_delimiter(self):
        node = TextNode(
            "This is **bold** text",
            TextType.TEXT
        )
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)

        self.assertEqual(new_nodes, [
            TextNode("This is ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
            TextNode(" text", TextType.TEXT),
        ])

    def test_italic_delimiter(self):
        node = TextNode(
            "This is _italic_ text",
            TextType.TEXT
        )
        new_nodes = split_nodes_delimiter([node], "_", TextType.ITALIC)

        self.assertEqual(new_nodes, [
            TextNode("This is ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" text", TextType.TEXT),
        ])

    def test_multiple_delimiters(self):
        node = TextNode(
            "A **bold** and **strong** word",
            TextType.TEXT
        )
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)

        self.assertEqual(new_nodes, [
            TextNode("A ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
            TextNode(" and ", TextType.TEXT),
            TextNode("strong", TextType.BOLD),
            TextNode(" word", TextType.TEXT),
        ])

    def test_non_text_node_unchanged(self):
        node = TextNode("bold", TextType.BOLD)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(new_nodes, [node])

    def test_missing_closing_delimiter_raises(self):
        node = TextNode(
            "This is **broken markdown",
            TextType.TEXT
        )
        with self.assertRaises(Exception):
            split_nodes_delimiter([node], "**", TextType.BOLD)


if __name__ == "__main__":
    unittest.main()
