class Veiculo:
    def __init__(self, marca, modelo):
        self._marca = marca
        self._modelo = modelo
        self._ligado = False

    def __str__(self):
        return f"Veiculo: {self.marca} {self.modelo}, Ligado: {'Sim' if self._ligado else 'Não'}"