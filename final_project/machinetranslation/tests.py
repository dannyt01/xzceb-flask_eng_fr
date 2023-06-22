from deep_translator import MyMemoryTranslator
from translator import english_to_french
from translator import french_to_english
import unittest

class TranslationTestCase1(unittest.TestCase):
    def test_translation(self):
        english_text = 'hello'
        french_translation = english_to_french(english_text)
        self.assertEqual(french_translation, 'bonjour')

class TranslationTestCase2(unittest.TestCase):
    def test_translation(self):
        french_text = 'bonjour'
        english_translation = french_to_english(french_text)
        self.assertEqual(english_translation, 'hello')


if __name__ == '__main__':
    unittest.main()