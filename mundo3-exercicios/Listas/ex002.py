numeros = list(range(1,10+1))
print(f"Lista Original:{numeros}")
print(f"Tam.Lista Original:{len(numeros)}\n")

escolha_ususario = int(input("Escolha Um numero[1/10]:"))
# verificando se o numero escolhido pelo usuario está presente na lista ou não. caso sim,
# vamos imprimir que encontramos o numero, caso nao, vamos dizer que o numero não existe na
# lista.#
if escolha_ususario in numeros:
    print(f'Encontrei o Numero: {escolha_ususario}!')
else:
    print(f"O numero {escolha_ususario} não Existe nessa lista!")

print("\nFim do Programa!")
