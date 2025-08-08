# Crie uma classe Veiculo e implemente pelo menos 3 subclasses de veículo. Os veiculos devem possuir pelo menos 4 atributos e ser capazes de acelerar, parar e mostrar informações.

class Veiculo:
    def __init__(self, marca, modelo, cor, velocidade):
        self.marca = marca
        self.modelo = modelo
        self.cor = cor
        self.velocidade = velocidade

    def acelerar(self):
        self.velocidade += 10
        print(
            f"O veículo está acelerando! E agora está se movendo a {self.velocidade} km/h")

    def parar(self):
        print("O veículo está parado!")

    def mostrarInformacoes(self):
        print(f'''
Informações do Veículo:  
Marca: {self.marca}
Modelo: {self.modelo}
Cor: {self.cor}
Velocidade: {self.velocidade} km/h
''')


class Carro(Veiculo):
    def __init__(self, marca, modelo, cor, velocidade):
        super().__init__(marca, modelo, cor, velocidade)


class Moto(Veiculo):
    def __init__(self, marca, modelo, cor, velocidade, ronco_do_motor):
        super().__init__(marca, modelo, cor, velocidade)
        self.ronco_do_motor = ronco_do_motor

    def mostrarInformacoes(self):
        print(f'''
Informações do Veículo:  
Marca: {self.marca}
Modelo: {self.modelo}
Cor: {self.cor}
Velocidade: {self.velocidade} km/h
Ronco do Motor: {self.ronco_do_motor}
''')

    def darOGrau(self):
        print("A moto está dando o grau! IEEEEEEEEEII")


class Onibus(Veiculo):
    def __init__(self, marca, modelo, cor, velocidade):
        super().__init__(marca, modelo, cor, velocidade)


v1 = Veiculo("Volkswagen", "Gol", "Azul", 120)
v1.acelerar()
v1.parar()
v1.mostrarInformacoes()

v2 = Onibus("Mercedes", "Sprinter", "Branco", 100)
v2.acelerar()
v2.parar()
v2.mostrarInformacoes()

v3 = Moto("Honda", "CBR500R", "Preto", 150, "RANDANDANDANDAN")
v3.acelerar()
v3.parar()
v3.mostrarInformacoes()
v3.darOGrau()

v4 = Carro("Fiat", "Uno", "Vermelho", 90)
v4.acelerar()
v4.parar()
v4.mostrarInformacoes()
