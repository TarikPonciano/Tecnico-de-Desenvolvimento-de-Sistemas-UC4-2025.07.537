class Conta:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo

    def ver_saldo(self):
        return f"Saldo: R$ {self.saldo:.2f}"

    def depositar(self, valor):
        if valor <= 0:
            print("Valor do depósito deve ser positivo!")
            return
        else:
            self.saldo += valor
            print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")

    def sacar(self, valor):
        if valor <= 0:
            print("Valor do saque deve ser positivo!")
            return
        elif valor > self.saldo:
            print(
                f"Saldo insuficiente para saque! Você tentou sacar R$ {valor:.2f} porém seu é R$ {self.saldo:.2f} ")
            return
        else:
            self.saldo -= valor
            print(f"Saque de R$ {valor:.2f} realizado com sucesso!")


if __name__ == "__main__":
    conta = Conta("João", 1000.00)
    conta.depositar(2000)
    conta.depositar(-500)
    print(conta.ver_saldo())
    conta.sacar(50000)
