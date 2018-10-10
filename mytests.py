'''utilisation du module unittest pour faire tous les tests'''
import unittest
from helloworld import *

#la Classe des tests:
class MyFirstTests(unittest.TestCase):
    #test de hello world:
    def test_hello(self):
        self.assertEqual(hello_world(),'hello world')
    #tests de calcul score en fonction des nom:
    def test_calculScore_Joseph(self):
        self.assertEqual(calculScore('Joseph',15),'66%')

    def test_calculScore_Marie(self):
        self.assertEqual(calculScore('Marie',33),'50%')

    def test_calculScore_Marc(self):
        self.assertEqual(calculScore('Marc',60),'43%')

    def test_calculScore_Ely(self):
        self.assertEqual(calculScore('Ely',28),'75%')
#lancement des tests:
if __name__=='__main__':
    unittest.main()