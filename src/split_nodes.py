#split-nodes.py

from textnode import TextType, TextNode

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    process_node = []

    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
        else:
            process_node = node.text.split(delimiter)
            if len(process_node) % 2 == 0:
                raise Exception("Unmatched delimiters - please correct")
            for i in range (len(process_node)):
                if process_node[i] == "":
                    continue
                elif i == 0 or i % 2 == 0:
                    new_nodes.append(TextNode(process_node[i], TextType.TEXT))
                else:
                    new_nodes.append(TextNode(process_node[i], text_type))
        
    return new_nodes
                