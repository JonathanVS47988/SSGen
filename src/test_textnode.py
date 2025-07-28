#test_textnode.py

import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_not_eq(self):
        node = TextNode("This is a text node", TextType.TEXT)
        node2 = TextNode("This is a txt node", TextType.TEXT)
        self.assertNotEqual(node, node2)

    def test_diff_type(self):
        node = TextNode("I'm a bold one", TextType.BOLD)
        node2 = TextNode("I'm italic!", TextType.ITALIC)
        self.assertNotEqual(node, node2)

    def test_no_url(self):
        node = TextNode("URL Link", TextType.LINK, "https://www.whatup.com")
        node2 = TextNode("URL Link not given", TextType.LINK)
        self.assertNotEqual(node, node2)

if __name__ == "__main__":
    unittest.main()