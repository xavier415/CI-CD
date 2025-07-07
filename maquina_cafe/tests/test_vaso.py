import unittest
from src.vaso import Vaso

class TestVaso(unittest.TestCase):

    def test_deberia_devolver_verdadero_si_existen_vasos(self):
        vaso = Vaso(2, 10)
        self.assertTrue(vaso.has_vasos(1))

    def test_deberia_devolver_falso_si_no_existen_vasos(self):
        vaso = Vaso(1, 10)
        self.assertFalse(vaso.has_vasos(2))

    def test_deberia_restar_vasos(self):
        vaso = Vaso(5, 10)
        vaso.give_vasos(1)
        self.assertEqual(vaso.get_cantidad_vasos(), 4)

