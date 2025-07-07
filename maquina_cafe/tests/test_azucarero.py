import unittest
from src.azucarero import Azucarero

class TestAzucarero(unittest.TestCase):

    def setUp(self):
        self.azucarero = Azucarero(10)

    def test_deberia_devolver_verdadero_si_hay_suficiente_azucar(self):
        self.assertTrue(self.azucarero.has_azucar(5))
        self.assertTrue(self.azucarero.has_azucar(10))

    def test_deberia_devolver_falso_si_no_hay_suficiente_azucar(self):
        self.assertFalse(self.azucarero.has_azucar(15))

    def test_deberia_restar_azucar(self):
        self.azucarero.give_azucar(5)
        self.assertEqual(self.azucarero.get_cantidad_azucar(), 5)
        self.azucarero.give_azucar(2)
        self.assertEqual(self.azucarero.get_cantidad_azucar(), 3)