from veiculo import Veiculo

class Moto(Veiculo):
    def __init__(self, marca, modelo, tipo):
        super().__init__(marca, modelo)
        self._tipo  = tipo 

    def __str__(self):
        return f"Moto: {self._marca} {self._modelo}, Tipo: {self._tipo}, Ligado: {'Sim' if self._ligado else 'Não'}"