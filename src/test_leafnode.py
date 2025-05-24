import unittest

from htmlnode import LeafNode

class TestLeafNode(unittest.TestCase):

    def test_no_tag(self):
        node = LeafNode(None, "This is my raw value", None)
        self.assertEqual(node.to_html(), node.value)

    def test_no_value(self):
        node = LeafNode("p", None)
        with self.assertRaises(ValueError):
            node.to_html()
    
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")
