import unittest
from src.maquina_cafe import MaquinaDeCafe

class TestMaquinaDeCafe(unittest.TestCase):

    def setUp(self):
        self.maquina = MaquinaDeCafe()

    def test_deberia_devolver_un_vaso_pequeno(self):
        vaso = self.maquina.get_tipo_vaso("pequeno")
        self.assertEqual(vaso.get_contenido(), 3)

    def test_deberia_devolver_un_vaso_mediano(self):
        vaso = self.maquina.get_tipo_vaso("mediano")
        self.assertEqual(vaso.get_contenido(), 5)

    def test_deberia_devolver_un_vaso_grande(self):
        vaso = self.maquina.get_tipo_vaso("grande")
        self.assertEqual(vaso.get_contenido(), 7)

    def test_deberia_devolver_no_hay_vasos(self):
        vaso = self.maquina.get_tipo_vaso("pequeno")
        resultado = self.maquina.get_vaso_de_cafe("pequeno", 10, 2)
        self.assertEqual(resultado, "No hay Vasos")

    def test_deberia_devolver_no_hay_cafe(self):
        self.maquina.cafetera = self.maquina.cafetera.__class__(5)
        resultado = self.maquina.get_vaso_de_cafe("pequeno", 1, 2)
        self.assertEqual(resultado, "No hay Cafe")

    def test_deberia_devolver_no_hay_azucar(self):
        self.maquina.azucarero = self.maquina.azucarero.__class__(2)
        resultado = self.maquina.get_vaso_de_cafe("pequeno", 1, 3)
        self.assertEqual(resultado, "No hay Azucar")

    def test_deberia_restar_cafe(self):
        self.maquina.get_vaso_de_cafe("pequeno", 1, 2)
        self.assertEqual(self.maquina.cafetera.get_cantidad_cafe(), 47)

    def test_deberia_restar_vaso(self):
        self.maquina.get_vaso_de_cafe("pequeno", 1, 2)
        cantidad_restante = self.maquina.vasos["pequeno"].get_cantidad_vasos()
        self.assertEqual(cantidad_restante, 4)

    def test_deberia_restar_azucar(self):
        self.maquina.get_vaso_de_cafe("pequeno", 1, 3)
        self.assertEqual(self.maquina.azucarero.get_cantidad_azucar(), 17)

    def test_deberia_devolver_felicitaciones(self):
        resultado = self.maquina.get_vaso_de_cafe("pequeno", 1, 3)
        self.assertEqual(resultado, "Felicitaciones")