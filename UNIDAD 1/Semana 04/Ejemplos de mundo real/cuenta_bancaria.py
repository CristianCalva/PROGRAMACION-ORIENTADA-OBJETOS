class CuentaBancaria:
    def __init__(self, numero_cuenta, titular, saldo=0.0):
        self.numero_cuenta = numero_cuenta
        self.titular = titular
        self.saldo = saldo

    def depositar(self, monto):
        if monto > 0:
            self.saldo += monto
            print(f"Depositados ${monto:.2f}. Saldo actual: ${self.saldo:.2f}")
        else:
            print("El monto a depositar debe ser positivo.")

    def retirar(self, monto):
        if 0 < monto <= self.saldo:
            self.saldo -= monto
            print(f"Retirados ${monto:.2f}. Saldo actual: ${self.saldo:.2f}")

    def consultar_saldo(self):
        print(f"Saldo actual: ${self.saldo:.2f}")
        return self.saldo


# crea una instancia de mi cuenta
if __name__ == "__main__":
    # Crear una cuenta bancaria
    cuenta = CuentaBancaria(numero_cuenta="123456789", titular="Paul Calva", saldo=3000.0)

    # Consultar saldo inicial
    cuenta.consultar_saldo()

    # Depositar dinero
    cuenta.depositar(500)

    # Retirar dinero
    cuenta.retirar(200)

    # Consultar saldo final
    cuenta.consultar_saldo()