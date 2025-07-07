class Azucarero:
    def __init__(self, cantidad_azucar: int):
        self._cantidad_azucar = cantidad_azucar

    def has_azucar(self, cantidad: int) -> bool:
        return self._cantidad_azucar >= cantidad

    def give_azucar(self, cantidad: int):
        if self.has_azucar(cantidad):
            self._cantidad_azucar -= cantidad

    def get_cantidad_azucar(self) -> int:
        return self._cantidad_azucar




