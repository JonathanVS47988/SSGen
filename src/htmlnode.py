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
        return f' href={self.props[0]} target={self.props[1]}'
    
    def __repr__(self):
        return f'HTMLNode:\n {self.tag} \n {self.value} \n {self.children} \n {self.props}'
