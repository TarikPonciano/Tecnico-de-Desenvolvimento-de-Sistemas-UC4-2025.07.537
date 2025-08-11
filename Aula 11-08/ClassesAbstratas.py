from abc import ABC, abstractmethod


class Pessoa(ABC):
    def __init__(self, nome, idade, cpf):
        super().__init__()
        self.nome = nome
        self.idade = idade
        self.cpf = cpf

    @abstractmethod
    def saudacao(self):
        # A pessoa deverá realizar uma saudação
        pass


class Funcionario(Pessoa):
    def __init__(self, nome, idade, cpf, salario):
        super().__init__(nome, idade, cpf)
        self.salario = salario

    def exibir_informacoes(self):
        print("Nome:", self.nome)

    def saudacao(self):
        print("Olá, sou o(a) funcionário(a) " + self.nome + "!")


class Gerente(Funcionario):
    def __init__(self, nome, idade, cpf, salario):
        super().__init__(nome, idade, cpf, salario)

    def exibir_informacoes(self):
        print(f'''
Informações do Gerente:
Nome: {self.nome}
Idade: {self.idade}
CPF: {self.cpf}
Salário: R$ {self.salario:.2f}
''')


f1 = Funcionario("Gilberto", 30, "98765432101", 5000.0)
f1.exibir_informacoes()

f2 = Gerente("Manoel", 35, "11111111111", 6000.0)
f2.exibir_informacoes()

f2.saudacao()
