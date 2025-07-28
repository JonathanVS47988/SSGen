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
    
#class LeafNode(HTMLNode):
#    def __init__(self, tag, value, props=None):
#        super().__init__(tag, value, props)

#    def to_html(self):
#        if self.value == None:
#            raise ValueError
#        if self.tag == None:
#            return f'{self.value}'
#        if self.props != None:
#            return f'<{self.tag}{self.props}>{self.value}</{tag}>'
#        else:
#            return f'<{self.tag}>{self.value}</{tag}>'