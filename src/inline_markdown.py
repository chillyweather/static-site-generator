import re
from textnode import TextNode

text_type_bold = "bold"
text_type_italic = "italic"
text_type_code = "code"
text_type_text = "text"


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    all_nodes = []
    for node in old_nodes:
        if not isinstance(node, TextNode):
            new_nodes.append(node)
        new_nodes = []
        node_arr = node.text.split(f"{delimiter}")
        if len(node_arr) % 2 == 0:
            raise Exception("not valid markdown syntax")
        if len(node_arr) == 1:
            all_nodes.append(TextNode(node_arr[0], text_type_text))
            continue
        for index, new_node in enumerate(node_arr):
            if len(new_node) == 0:
                continue
            if index % 2 == 1:
                new_node = TextNode(new_node, text_type)
            else:
                new_node = TextNode(new_node, text_type_text)
            new_nodes.append(new_node)
        all_nodes.extend(new_nodes)

    return all_nodes


def extract_markdown_images(string):
    matches = re.findall(r"!\[(.*?)\]\((.*?)\)", string)
    return matches


def extract_markdown_links(string):
    matches = re.findall(r"\[(.*?)\]\((.*?)\)", string)
    return matches
