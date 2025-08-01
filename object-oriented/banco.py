class ContaBancaria:
    def __init__(self, titular="", saldo="0"):
        self._titular = titular
        self._saldo = saldo
        self._ativo = False

    def __str__(self):
        return f'{self._titular} é o titular da conta e possui o saldo de {self._saldo} a conta esta {self.ativo}'
    
    def ativar_conta(self):
        self._ativo = not self._ativo

    @property
    def ativo(self):
        return 'Ativo' if self._ativo else 'Desativado'
        
conta1 = ContaBancaria('John Due', '22.000,00')
conta2 = ContaBancaria('Jhon Lore', '21.653,00')

print(conta1)

conta2.ativar_conta()
print(conta2)

print(conta1._titular)