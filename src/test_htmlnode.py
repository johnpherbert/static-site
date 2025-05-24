import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_props(self):
        node1 = HTMLNode("p","hello",None,{"my_props":"hello_everyone","second_prop":"lets_go"})
        expected_string = " my_props=\"hello_everyone\" second_prop=\"lets_go\""
        self.assertEqual(node1.props_to_html(), expected_string)

    def test_empty_props(self):
        node1 = HTMLNode("p","hello",None,None)
        self.assertEqual(node1.props_to_html(), "")

    def test_image_link(self):
        node1 = HTMLNode("img",None,None,{"href":"https://www.google.com","target":"_blank"})
        expected_string = " href=\"https://www.google.com\" target=\"_blank\""
        self.assertEqual(node1.props_to_html(), expected_string)