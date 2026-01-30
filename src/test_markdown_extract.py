import unittest

from markdown_extract import (
    extract_markdown_images,
    extract_markdown_links,
)


class TestMarkdownExtract(unittest.TestCase):
    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual(
            [("image", "https://i.imgur.com/zjjcJKZ.png")],
            matches
        )

    def test_extract_multiple_images(self):
        text = (
            "![one](url1.png) and ![two](url2.jpg)"
        )
        matches = extract_markdown_images(text)
        self.assertListEqual(
            [("one", "url1.png"), ("two", "url2.jpg")],
            matches
        )

    def test_extract_markdown_links(self):
        text = (
            "This is a [link](https://example.com)"
        )
        matches = extract_markdown_links(text)
        self.assertListEqual(
            [("link", "https://example.com")],
            matches
        )

    def test_extract_multiple_links(self):
        text = (
            "[one](url1) and [two](url2)"
        )
        matches = extract_markdown_links(text)
        self.assertListEqual(
            [("one", "url1"), ("two", "url2")],
            matches
        )

    def test_links_do_not_match_images(self):
        text = (
            "![img](img.png) and [link](site.com)"
        )
        matches = extract_markdown_links(text)
        self.assertListEqual(
            [("link", "site.com")],
            matches
        )

    def test_no_matches(self):
        text = "Just plain text"
        self.assertListEqual([], extract_markdown_images(text))
        self.assertListEqual([], extract_markdown_links(text))


if __name__ == "__main__":
    unittest.main()
