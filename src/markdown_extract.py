import re


def extract_markdown_images(text):
    """
    Returns a list of tuples: (alt_text, url)
    """
    pattern = r"!\[([^\[\]]*)\]\(([^\(\)]*)\)"
    return re.findall(pattern, text)


def extract_markdown_links(text):
    """
    Returns a list of tuples: (anchor_text, url)
    """
    pattern = r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)"
    return re.findall(pattern, text)

