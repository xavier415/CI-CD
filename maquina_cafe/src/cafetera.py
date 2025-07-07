class Cafetera:
    def __init__(self, cantidad_cafe: int):
        self._cantidad_cafe = cantidad_cafe  # en oz

    def has_cafe(self, cantidad: int) -> bool:
        return self._cantidad_cafe >= cantidad

    def give_cafe(self, cantidad: int):
        if self.has_cafe(cantidad):
            self._cantidad_cafe -= cantidad

    def get_cantidad_cafe(self) -> int:
        return self._cantidad_cafe