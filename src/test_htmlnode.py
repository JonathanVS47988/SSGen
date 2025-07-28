#test_htmlnode.py

import unittest

from htmlnode import HTMLNode#, LeafNode

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
        node = HTMLNode("<code>", "class Example Code:")

    def test_bold_type(self):
        node = HTMLNode("<b>", "BOLD meh!")

    #def test_leaf_to_html_p(self):
    #    node = LeafNode("p", "Hello, world!")
    #    self.assertEqual(node.to_html(), "<p>Hello, world!</p>")       

if __name__ == "__main__":
    unittest.main()