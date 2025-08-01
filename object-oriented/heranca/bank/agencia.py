from banco import Banco

class Agencia(Banco):
    def __init__(self, nome, endereco, numero):
        super().__init__(nome, endereco)
        self._numero = numero

    def __str__(self):
        return f"nome: {self._nome}, endereco: {self._endereco}, numero: {self._numero}"


agencia1 = Agencia("Banco do Brasil", "Rua A, 123", "001")

print(agencia1)  # Saída: nome: Banco do Brasil, endereco: Rua A, 123, numero: 001