#test_htmlnode.py

import unittest

from htmlnode import HTMLNode

class TestTextNode(unittest.TestCase):
    def test_href(self):
        self.props = {
            "href": "https://www.boot.dev",
            "target": "_blank",
        }
        node = HTMLNode("<a>",None,None,self.props)
        print(HTMLNode)

    def test_generic_1(self):
        node = HTMLNode("<h1>", "Test Heading 1")

    def test_code_type(self):
        node = HTMLNode("<code>", "class Example Code:")

    def test_bold_type(self):
        node = HTMLNode("<b>", "BOLD meh!")       

if __name__ == "__main__":
    unittest.main()