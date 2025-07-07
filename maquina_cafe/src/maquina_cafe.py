from .cafetera import Cafetera
from .vaso import Vaso
from .azucarero import Azucarero

class MaquinaDeCafe:
    def __init__(self):
        self.vasos = {
            'pequeno': Vaso(5, 3),
            'mediano': Vaso(5, 5),
            'grande': Vaso(5, 7)
        }
        self.cafetera = Cafetera(50)
        self.azucarero = Azucarero(20)

    def get_tipo_vaso(self, tipo: str) -> Vaso:
        return self.vasos.get(tipo)

    def get_vaso_de_cafe(self, tipo: str, cantidad_vasos: int, cantidad_azucar: int) -> str:
        vaso = self.get_tipo_vaso(tipo)
        if not vaso or not vaso.has_vasos(cantidad_vasos):
            return "No hay Vasos"
        if not self.cafetera.has_cafe(vaso.get_contenido() * cantidad_vasos):
            return "No hay Cafe"
        if not self.azucarero.has_azucar(cantidad_azucar):
            return "No hay Azucar"

        vaso.give_vasos(cantidad_vasos)
        self.cafetera.give_cafe(vaso.get_contenido() * cantidad_vasos)
        self.azucarero.give_azucar(cantidad_azucar)
        return "Felicitaciones"

