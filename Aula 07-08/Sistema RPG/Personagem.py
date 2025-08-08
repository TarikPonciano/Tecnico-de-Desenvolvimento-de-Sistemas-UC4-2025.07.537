class Personagem:
    def __init__(self, nome, classe, nivel):
        self._nome = nome
        self.classe = classe
        self.__nivel = nivel

        if self.classe == "Guerreiro":
            self.vida = 100
            self.ataque = 10
            self.defesa = 30
        elif self.classe == "Mago":
            self.vida = 60
            self.ataque = 30
            self.defesa = 10
        elif self.classe == "Arqueiro":
            self.vida = 80
            self.ataque = 20
            self.defesa = 20

    def subir_nivel(self):
        self.__nivel += 1
        if self.classe == "Guerreiro":
            self.vida += 10
            self.ataque += 2
            self.defesa += 5
        elif self.classe == "Mago":
            self.vida += 5
            self.ataque += 5
            self.defesa += 2
        elif self.classe == "Arqueiro":
            self.vida += 8
            self.ataque += 3
            self.defesa += 3

    def levar_dano(self, ataque):
        dano = round(5 * (ataque/self.defesa))
        self.vida -= dano
        print(
            f"{self._nome} levou {dano:.2f} de dano do golpe.")
        if self.vida <= 0:
            self.vida = 0
            # print(f"{self._nome} foi derrotado!")

    def atacar(self, alvo):
        print(f"{self._nome} ataca {alvo._nome}!")
        alvo.levar_dano(self.ataque)

    def exibir_status(self):
        print(f"Nome: {self._nome}")
        print(f"Classe: {self.classe}")
        print(f"Nível: {self.__nivel}")
        print(f"Vida: {self.vida}")
        print(f"Ataque: {self.ataque}")
        print(f"Defesa: {self.defesa}")
