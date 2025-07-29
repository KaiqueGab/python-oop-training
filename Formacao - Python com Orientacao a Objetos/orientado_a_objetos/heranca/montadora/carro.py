from veiculo import Veiculo

class Carro(Veiculo):
    def __init__(self, marca, modelo, numero_portas):
        super().__init__(marca, modelo)
        self._numero_portas = numero_portas

    def __str__(self):
        return f"Carro: {self._marca} {self._modelo}, Portas: {self._numero_portas}, Ligado: {'Sim' if self._ligado else 'Não'}"