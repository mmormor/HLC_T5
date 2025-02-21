class CuentBanca:
    def __init__(self, saldo):
        self.saldo = saldo
    def deposito(self, sumar):
        self.sumar = sumar
        self.saldo += self.sumar
    def ver_sal(self):
        return f"El saldo es de {self.saldo}"
    def retir(self, restar):
        self.restar = restar
        self.saldo -= self.restar
cuenta = CuentBanca(1000)
cuenta.deposito(500)
cuenta.retir(300)
print(cuenta.ver_sal())
