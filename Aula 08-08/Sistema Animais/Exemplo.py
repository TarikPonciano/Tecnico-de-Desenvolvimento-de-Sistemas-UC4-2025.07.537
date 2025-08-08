class Pokemon:
    def __init__(self, name, level, hp, attack, defense, type):
        self.name = name
        self.level = level
        self.hp = hp
        self.attack = attack
        self.defense = defense
        self.type = type

    def atacar(self):
        print(f"{self.name} atacou!")

class PokemonFogo(Pokemon):
    def __init__(self, name, level, hp, attack, defense):
        super().__init__(name, level, hp, attack, defense, "Fogo")
        self.vantagens = ["Grama", "Elétrico"]
        self.desvantagens = ["Água", "Terra"]

class Charmander(PokemonFogo):
    def __init__(self, name, level, hp, attack, defense):
        super().__init__(name, level, hp, attack, defense)
    def lanca_chamas(self):
        print(f"{self.name} lançou chamas!")


class Pikachu(Pokemon):
    def __init__(self, name, level, hp, attack, defense, IV):
        super().__init__(name, level, hp, attack, defense, "Electric")
        self.IV = IV
        self.evolucao = "Raichu"
    def atacar(self):
        print(f"{self.name} atacou com um choque do trovão!")
