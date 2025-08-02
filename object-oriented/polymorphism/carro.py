from veiculo import Veiculo

class Carro(Veiculo):
    def __init__(self, modelo, marca, cor):
        super().__init__(marca, modelo)
        self._cor = cor

    def __str__(self):
        return f"Carro 1: {self._marca} {self._modelo} | Cor: {self._cor}"

    def ligar(self):
        return f"\n{self._marca} {self._modelo} está ligado."
    