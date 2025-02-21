class CuentaBancaria:
    def __init__(self, balance):
        self.balance = balance

    def ingresar(self, cantidad):
        self.balance += cantidad

    def retirar(self, cantidad):
        self.balance -= cantidad

    def mostrar_saldo(self):
        return f"Saldo actual: {self.balance}"

mi_cuenta = CuentaBancaria(1000)
mi_cuenta.ingresar(500)
mi_cuenta.retirar(300)
print(mi_cuenta.mostrar_saldo())
