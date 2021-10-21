import unittest
#from translator import english_to_french, french_to_english
import machinetranslation

class Teste2f(unittest.TestCase):
    def test1(self):
        self.assertEqual(translator.english_to_french(''), None) # test when 2 is given as input the output is 4.
    
    def test2(self):
        self.assertEqual(translator.english_to_french('Hello'), 'Bonjour')  # test when 3.0 is given as input the output is 9.0.
        
class Testf2e(unittest.TestCase):
    def test1(self):
        self.assertEqual(translator.french_to_english(''), None) # test when 2 is given as input the output is 4.
        
    def test2(self):
        self.assertEqual(translator.french_to_english('Bonjour'), 'Hello') # test when -3.1 is given as input the output is -6.2.

if __name__ == "__main__":
    unittest.main()