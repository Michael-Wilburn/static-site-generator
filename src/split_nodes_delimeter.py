from textnode import TextNode, TextType


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []

    for node in old_nodes:
        # Solo procesamos nodos de texto plano
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue

        parts = node.text.split(delimiter)

        # Si no hay pares válidos de delimitadores → error
        if len(parts) % 2 == 0:
            raise Exception("Invalid Markdown syntax: missing closing delimiter")

        for i, part in enumerate(parts):
            if part == "":
                continue

            if i % 2 == 0:
                # Texto normal
                new_nodes.append(TextNode(part, TextType.TEXT))
            else:
                # Texto delimitado
                new_nodes.append(TextNode(part, text_type))

    return new_nodes

