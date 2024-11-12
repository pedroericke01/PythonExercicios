# Tupulas são imutaveis, ou seja, não podemos inserir novos itens a ela durante sua execução
# apenas quando o programa não está executando. #

print("\n{:_^35}\n".format(" TUPULAS SÃO IMUTÁVEIS "))

lanches = ("Hamburguer", "Suco", "Pizza", "Pudim")
for comida in lanches:
    print(f"Eu Vou comer {comida}")
print("\nFim do Programa!")
