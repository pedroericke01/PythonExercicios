print("\n{:_^35}\n".format(" TUPULAS SÃO IMUTAVEIS "))

lanche = ("Hamburguer", "Suco", "Pizza", "Pudim", "Batata Frita")
print(f"Tupula Original:{lanche}\n")

print(f"Tamanho da Tupula:{len(lanche)} elementos\n")

for posicao, comida in enumerate(lanche):
    print(f"Eu vou Comer {comida} no índice {posicao} da tupula")
print("\nFim")
