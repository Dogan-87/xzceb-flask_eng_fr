import unittest
from translator import englishToFrench, frenchToEnglish

class Teste2f(unittest.TestCase):
    def test1(self):
        self.assertEqual(englishToFrench(), ) # test when 2 is given as input the output is 4.
        self.assertEqual(englishToFrench('Hello'), 'Bonjour')  # test when 3.0 is given as input the output is 9.0.
        #self.assertNotEqual(square(-3), -9)  # test when -3 is given as input the output is not -9.


class Testf2e(unittest.TestCase):
    def test1(self):
        self.assertEqual(frenchToEnglish(), ) # test when 2 is given as input the output is 4.
        self.assertEqual(frenchToEnglish('Bonjour'), 'Hello') # test when -3.1 is given as input the output is -6.2.
        #self.assertEqual(double(0), 0) # test when 0 is given as input the output is 0.

if __name__ == "__main__":
    unittest.main()