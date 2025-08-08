class Animal:
    def __init__(self, nome, cor):
        self.nome = nome
        self.cor = cor

    def comer(self):
        print(f"{self.nome} está comendo")

    def informacoes(self):
        print(f'''Nome: {self.nome}
              Cor: {self.cor}''')


class Gato(Animal):
    def __init__(self, nome, cor):
        super().__init__(nome, cor)


class Cachorro(Animal):
    def __init__(self, nome, cor):
        super().__init__(nome, cor)


class Coelho(Animal):
    def __init__(self, nome, cor):
        super().__init__(nome, cor)


a1 = Animal("Girafa", "Amararela")

a2 = Gato("Gato", "Preto")

a3 = Cachorro("Totó", "Caramelo")

a4 = Coelho("Hannah", "Branco")

a1.comer()
a2.comer()
a3.comer()
a4.comer()

a4.informacoes()
