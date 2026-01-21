import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq_same_text_type_no_url(self):
        node1 = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node1, node2)

    def test_not_eq_different_text(self):
        node1 = TextNode("Text one", TextType.BOLD)
        node2 = TextNode("Text two", TextType.BOLD)
        self.assertNotEqual(node1, node2)

    def test_not_eq_different_text_type(self):
        node1 = TextNode("Same text", TextType.BOLD)
        node2 = TextNode("Same text", TextType.ITALIC)
        self.assertNotEqual(node1, node2)

    def test_eq_with_url(self):
        node1 = TextNode(
            "Boot.dev",
            TextType.LINK,
            "https://www.boot.dev"
        )
        node2 = TextNode(
            "Boot.dev",
            TextType.LINK,
            "https://www.boot.dev"
        )
        self.assertEqual(node1, node2)

    def test_not_eq_different_url(self):
        node1 = TextNode(
            "Boot.dev",
            TextType.LINK,
            "https://www.boot.dev"
        )
        node2 = TextNode(
            "Boot.dev",
            TextType.LINK,
            "https://www.google.com"
        )
        self.assertNotEqual(node1, node2)


if __name__ == "__main__":
    unittest.main()
