import unittest
from .translator import english_to_french, french_to_english

class TestTranslator(unittest.TestCase):

    def test_english_to_french_hello(self):
        english_text = 'Hello'
        french_text = english_to_french(english_text)
        self.assertEqual(french_text, 'Bonjour')

    def test_english_to_french_bonjour(self):
        english_text = 'Bonjour'
        french_text = english_to_french(english_text)
        self.assertEqual(french_text, 'Bonjour')

if __name__ == '__main__':
    unittest.main()