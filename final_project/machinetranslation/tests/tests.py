import unittest
from translator import english_to_french, french_to_english

class TestFrenchToEnglish(unittest.TestCase):
    def test_for_valid_input(self):
        self.assertEqual(french_to_english('Bonjour'), 'Hello')

    def test_for_negative_result(self):
        self.assertNotEqual(french_to_english('Bonjour'), 'Bonjour')

    def test_for_null(self) :
        self.assertEqual(french_to_english(), 'Invalid input')

class TestEnglishToFrench(unittest.TestCase):
    def test_for_valid_input(self):
        self.assertEqual(english_to_french('Hello'), 'Bonjour')

    def test_for_negative_result(self):
        self.assertNotEqual(english_to_french('Hello'), 'Hello')

    def test_for_null(self) :
        self.assertEqual(english_to_french(), 'Invalid input')



unittest.main()

