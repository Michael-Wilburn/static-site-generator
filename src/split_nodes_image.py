from textnode import TextNode, TextType
from markdown_extract import extract_markdown_images

def split_nodes_image(old_nodes):
    new_nodes = []

    for node in old_nodes:
        # Only split TEXT nodes
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue

        images = extract_markdown_images(node.text)

        # No images → keep node as-is
        if not images:
            new_nodes.append(node)
            continue

        remaining_text = node.text

        for alt_text, url in images:
            markdown = f"![{alt_text}]({url})"
            before, after = remaining_text.split(markdown, 1)

            if before:
                new_nodes.append(TextNode(before, TextType.TEXT))

            new_nodes.append(TextNode(alt_text, TextType.IMAGE, url))

            remaining_text = after

        if remaining_text:
            new_nodes.append(TextNode(remaining_text, TextType.TEXT))

    return new_nodes
