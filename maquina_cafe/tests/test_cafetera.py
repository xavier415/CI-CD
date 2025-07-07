import unittest
from src.cafetera import Cafetera

class TestCafetera(unittest.TestCase):

    def test_deberia_devolver_verdadero_si_existe_cafe(self):
        cafetera = Cafetera(10)
        self.assertTrue(cafetera.has_cafe(5))

    def test_deberia_devolver_falso_si_no_existe_cafe(self):
        cafetera = Cafetera(10)
        self.assertFalse(cafetera.has_cafe(11))

    def test_deberia_restar_cafe(self):
        cafetera = Cafetera(10)
        cafetera.give_cafe(7)
        self.assertEqual(cafetera.get_cantidad_cafe(), 3)