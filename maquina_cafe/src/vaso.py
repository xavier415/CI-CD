class Vaso:
    def __init__(self, cantidad_vasos: int, contenido: int):
        self._cantidad_vasos = cantidad_vasos
        self._contenido = contenido  # en oz

    def has_vasos(self, cantidad: int) -> bool:
        return self._cantidad_vasos >= cantidad

    def give_vasos(self, cantidad: int):
        if self.has_vasos(cantidad):
            self._cantidad_vasos -= cantidad

    def get_cantidad_vasos(self) -> int:
        return self._cantidad_vasos

    def get_contenido(self) -> int:
        return self._contenido