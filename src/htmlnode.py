#htmlnode.py

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