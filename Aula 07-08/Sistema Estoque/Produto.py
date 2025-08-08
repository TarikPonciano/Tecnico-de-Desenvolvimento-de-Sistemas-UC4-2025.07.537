class Produto:
    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = float(preco)
        self.quantidade = int(quantidade)

    def adicionar_estoque(self, quantidade):
        if quantidade < 0:
            print("Quantidade inválida!")
            return
        else:
            self.quantidade += quantidade
            print(f"Estoque atualizado! Novo estoque: {self.quantidade}")

    def remover_estoque(self, quantidade):
        if quantidade < 0:
            print("Quantidade inválida!")
            return
        elif quantidade > self.quantidade:
            print("Estoque insuficiente!")
            return
        else:
            self.quantidade -= quantidade
            print(f"Estoque atualizado! Novo estoque: {self.quantidade}")

    def consultar_estoque(self):
        print(
            f"Estoque atual: {self.quantidade} unidades de {self.nome} disponíveis.")
        return self.quantidade

    def aplicar_desconto_temporario(self, percentual):
        preco_descontado = self.preco * (1 - percentual/100)
        return preco_descontado

    def aplicar_desconto_permanente(self, percentual):
        self.preco = self.preco * (1 - percentual/100)
        return self.preco

