import unittest
from translator import english_to_french, french_to_english


class Teste2f(unittest.TestCase):
    def test1(self):
        self.assertEqual(english_to_french(''), None) 
    def test2(self):
        self.assertEqual(english_to_french('Hello'), 'Bonjour') 
        self.assertNotEqual(english_to_french('Hello'), 'Hola')  

class Testf2e(unittest.TestCase):
    def test1(self):
        self.assertEqual(french_to_english(''), None) 
    def test2(self):
        self.assertEqual(french_to_english('Bonjour'), 'Hello') 
        self.assertNotEqual(english_to_french('Bonjour'), 'Hola')  

if __name__ == "__main__":
    unittest.main()
