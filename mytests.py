'''utilisation du module unittest pour faire tous les tests de la fonction hello world'''
import unittest
from helloworld import *

class MyFirstTests(unittest.TestCase):

    def test_hello(self):
        self.assertEqual(hello_world(),'hello world')

    def test_calculScore_Joseph(self):
        self.assertEqual(calculScore('Joseph',15),'66%')

    def test_calculScore_Marie(self):
        self.assertEqual(calculScore('Marie',33),'50%')

    def test_calculScore_Marc(self):
        self.assertEqual(calculScore('Marc',60),'43%')

    def test_calculScore_Ely(self):
        self.assertEqual(calculScore('Ely',28),'75%')

if __name__=='__main__':
    unittest.main()