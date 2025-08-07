from Produto import Produto

p1 = Produto("Camiseta", 29.90, 0)

print(
    f"Preço com desconto permanente: R${p1.aplicar_desconto_permanente(10):.2f}")
if (p1.consultar_estoque() > 0):
    print("Produto está disponível para venda.")
else:
    print("Produto esgotado.")
