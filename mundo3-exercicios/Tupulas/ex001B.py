lanches = ("Hamburguer", "Suco", "Pizza", "Pudim", "Batata Frita")

# identificando o tamanho da tupula, sabemos que são 5 elementos:
# print(len(lanches))

# loop que imprime os elementos da tupula lanche que estão na posição/indice da variável de
# controle Cont, dessa forma:
# cont 0 == "HAMBURGUER
# cont 1 == "suco"
# assim em diante até o ultimo elemento válido da minha tupula #
for cont in range(0, len(lanches)):
    print(f"Eu vou comer {lanches[cont]} no indice {cont} da tupula")
print("\nFim")
