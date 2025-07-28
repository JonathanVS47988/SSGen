#test_htmlnode.py

import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode

class TestTextNode(unittest.TestCase):
    def test_href(self):
        self.props = {
            "href": "https://www.boot.dev",
            "target": "_blank",
        }
        node = HTMLNode(None,None,None,self.props)
        self.assertEqual(node.props_to_html(), ' href="https://www.boot.dev" target="_blank"') 

    def test_generic_1(self):
        node = HTMLNode("h1", "Test Heading 1")
        self.assertEqual(repr(node), 'HTMLNode:\n h1 \n Test Heading 1 \n None \n None')

    def test_code_type(self):
        node = HTMLNode("<code>", "class Example Code:",None, None)
        self.assertEqual(repr(node), 'HTMLNode:\n <code> \n class Example Code: \n None \n None')

    def test_bold_type(self):
        node = HTMLNode("<b>", "BOLD meh!")
        self.assertEqual(repr(node), 'HTMLNode:\n <b> \n BOLD meh! \n None \n None')

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")  

    def test_leaf_to_html_h1(self):
        node = LeafNode("h1", "Hello, world!")
        self.assertEqual(node.to_html(), "<h1>Hello, world!</h1>")
    
    def test_leaf_to_html_code(self):
        node = LeafNode("code", "Hello, world!")
        self.assertEqual(node.to_html(), "<code>Hello, world!</code>")

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_to_html_great_grand(self):
        great_grandchild_node = LeafNode("b", "great_grandchild")
        grandchild_node = ParentNode("b", [great_grandchild_node])
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b><b>great_grandchild</b></b></span></div>",
        )

    #def test_to_html_no_children(self):
    #    parent_node = ParentNode("div", None)
    #    self.assertEqual(
    #        parent_node.to_html(),
    #        "Children are required.  Please pass the appropriate object(s).",
    #    )              

if __name__ == "__main__":
    unittest.main()