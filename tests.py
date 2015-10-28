import unittest
import parse_message as p
import json

class TestParseMessage(unittest.TestCase):

    def test_parse_mentions(self):
        self.assertEqual(p.parse('Hi @bob'), '''{\n    "mentions":[\n        "bob"\n    ]\n}''')

    def test_parse_emoticons(self):
        expected = '''{\n    "emoticons":[\n        "megusta",\n        "coffee"\n    ]\n}'''
        self.assertEqual(p.parse('Good morning! (megusta) (coffee)'), expected)

    def test_parse_urls(self):
        actual = p.parse("I really like http://www.google.com")
        actual = json.loads(actual)
        self.assertIn(u'links', actual)
        self.assertEqual(len(actual[u'links']), 1)
        self.assertIn(u'url', actual[u'links'][0])
        self.assertEqual(actual[u'links'][0][u'url'], 'http://www.google.com')
        self.assertIn(u'title', actual[u'links'][0])
        self.assertTrue(len(actual[u'links'][0][u'title']) >0)
        
if __name__ == '__main__':
    unittest.main()


