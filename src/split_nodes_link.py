from textnode import TextNode, TextType
from markdown_extract import extract_markdown_links

def split_nodes_link(old_nodes):
    new_nodes = []

    for node in old_nodes:
        # Only split TEXT nodes
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue

        links = extract_markdown_links(node.text)

        # No links → keep node as-is
        if not links:
            new_nodes.append(node)
            continue

        remaining_text = node.text

        for link_text, url in links:
            markdown = f"[{link_text}]({url})"
            before, after = remaining_text.split(markdown, 1)

            if before:
                new_nodes.append(TextNode(before, TextType.TEXT))

            new_nodes.append(TextNode(link_text, TextType.LINK, url))

            remaining_text = after

        if remaining_text:
            new_nodes.append(TextNode(remaining_text, TextType.TEXT))

    return new_nodes
