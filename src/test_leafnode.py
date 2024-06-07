import unittest

from htmlnode import LeafNode


class TestLeafNode(unittest.TestCase):
    def test_props(self):
        expected1 = '<a href="https://www.google.com">Click me!</a>'
        expected2 = ' href="https://www.google.com" target="_blank"'
        tested1 = LeafNode(
            "a", "Click me!", {"href": "https://www.google.com"}
        ).to_html()
        self.assertEqual(expected1, tested1)


if __name__ == "__main__":
    unittest.main()
