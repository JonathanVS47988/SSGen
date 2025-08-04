#htmlnode.py

#from textnode import TextType, TextNode
#from extract_funcs import *
from split_nodes import *

class HTMLNode:

    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        html_string = ""
        for key, value in self.props.items():
            html_string += f' {key}="{value}"'
        return html_string

    def __repr__(self):
        return f'HTMLNode:\n {self.tag} \n {self.value} \n {self.children} \n {self.props}'
    
class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, props)

    def to_html(self):
        if self.value == None:
            raise ValueError("No value submitted.  Please submit contents to convert.")
        if self.tag == None:
            return f'{self.value}'
        if self.props != None:
            return f'<{self.tag}{self.props}>{self.value}</{self.tag}>'
        else:
            return f'<{self.tag}>{self.value}</{self.tag}>'
        
class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        self.tag = tag
        self.children = children
        self.props = props

    def to_html(self):
        if self.tag == None:
            raise ValueError("No tag.  Please pass a tag.")
        if self.children == None:
            raise ValueError("Children are required.  Please pass the appropriate object(s).")
        
        child_construct = ""
    
        for child in self.children:
            child_construct += child.to_html()
    
        return f'<{self.tag}>' + child_construct + f'</{self.tag}>'

def text_node_to_html_node(text_node):
    if not isinstance(text_node.text_type, TextType):
        raise Exception("Not a valid type.")
        
    if text_node.text_type == TextType.TEXT:
        return LeafNode(None, text_node.text)
    elif text_node.text_type == TextType.BOLD:
        return LeafNode("b", text_node.text)
    elif text_node.text_type == TextType.ITALIC:
        return LeafNode("i", text_node.text)
    elif text_node.text_type == TextType.CODE:
        return LeafNode("code", text_node.text)
    elif text_node.text_type == TextType.LINK:
        return LeafNode("a", text_node.text, "href")
    elif text_node.text_type == TextType.IMAGE:
        return LeafNode("img","","src" "alt")
    
def text_to_children(text):
    HTMLNode_list = []
    
    text_node_list = text_to_textnodes(text)
    for node in text_node_list:
        HTMLNode_list.append(text_node_to_html_node(node))
    
    return HTMLNode_list

def split_list_nodes(block, type):
    if type == 'ol':
        process_node = block.split("\n")
        InnerNodes_List = []
        for item in process_node:
            item_text = item[3:]
            item_children = text_to_children(item_text)
            InnerNodes_List.append(ParentNode("li", item_children))
        return ParentNode("ol", InnerNodes_List)
    
    if type == 'ul':
        process_node = block.split('\n')
        InnerNodes_List = []
        for item in process_node:
            item_text = item[2:]
            item_children = text_to_children(item_text)
            InnerNodes_List.append(ParentNode("li", item_children))
        return ParentNode("ol", InnerNodes_List)         

def markdown_to_html_node(markdown):
    md_blocks = markdown_to_blocks(markdown)
    Master_HTMLNode_List = []

    for block in md_blocks:
        typed_block = block_to_block_type(block)
        
        if typed_block == BlockType.CODE:
            if not block.startswith("```") or not block.endswith("```"):
                raise ValueError("invalid code block")
            node = block[4:-3]
            child = text_node_to_html_node(TextNode(node,TextType.TEXT))
            P_node = ParentNode("code",[child])
            Master_HTMLNode_List.append(ParentNode("pre", [P_node]))
        
        elif typed_block == BlockType.HEADING:
            heading_level = 0
            for char in block:
                if char == '#':
                    heading_level +=1
                else:
                    break
            if heading_level + 1 >= len(block):
                raise ValueError(f"invalid heading level: {heading_level}")

            heading_tag = f"h{heading_level}"
            heading_text = block[heading_level + 1 :]
            HTMLNode_list = text_to_children(heading_text)
            P_node = ParentNode(heading_tag, HTMLNode_list)
            Master_HTMLNode_List.append(P_node)
        
        elif typed_block == BlockType.QUOTE:
            lines = block.split('\n')
            mod_lines = []
            for line in lines:
                if not line.startswith(">"):
                    raise ValueError("invalid quote block")
                mod_lines.append(line.lstrip(">").strip())
            block_text = " ".join(mod_lines)
            HTMLNode_list = text_to_children(block_text)
            P_node = ParentNode("blockquote", HTMLNode_list)
            Master_HTMLNode_List.append(P_node)
        
        elif typed_block == BlockType.UNORDERED_LIST:
            Master_HTMLNode_List.append(split_list_nodes(block, 'ul'))
        
        elif typed_block == BlockType.ORDERED_LIST:
            Master_HTMLNode_List.append(split_list_nodes(block, 'ol'))
        
        else:
            lines = block.split("\n")
            paragraph = " ".join(lines)
            HTMLNode_list = text_to_children(paragraph)
            P_node = ParentNode("p", HTMLNode_list)
            Master_HTMLNode_List.append(P_node)

    return ParentNode("div", Master_HTMLNode_List, None)