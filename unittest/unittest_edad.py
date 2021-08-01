import unittest
import datetime
from fecha_edad import edad

class TestEdad(unittest.TestCase):
    def test_edad(self):
        #prueba de cuando conocemos la edad 
        print("prueba de la edad segun su año de nacimiento: ")
        self.assertAlmostEqual(edad(2000), 21)