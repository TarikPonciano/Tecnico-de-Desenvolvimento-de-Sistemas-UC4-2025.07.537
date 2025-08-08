from Personagem import Personagem

p1 = Personagem("Arthur", "Guerreiro", 1)

p2 = Personagem("Merlin", "Mago", 1)

print(p2._nome)

p2.subir_nivel()
p2.subir_nivel()

while True:
    p1.atacar(p2)
    if p2.vida <= 0:
        print(f"{p2._nome} foi derrotado!")
        p1.subir_nivel()
        break
    else:
        p2.atacar(p1)
        if p1.vida <= 0:
            print(f"{p1._nome} foi derrotado!")
            p2.subir_nivel()
            break


p1.exibir_status()
p2.exibir_status()
