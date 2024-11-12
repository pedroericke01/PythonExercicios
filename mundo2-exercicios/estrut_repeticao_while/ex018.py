# programa que lê o nome e o preco de vários produtos, o programa deverá perguntar se o
# usuario deseja continuar a inserir outros produtos ou não e no final deverá apresentar:

# 1- O Total gasto na compra
# 2- Quantos produtos custam mais de R$1000
# 3- Nome do Produto mais barato #

print("\n{:=^40}\n".format(" BANCO HORTFRUT "))

resposta_usuario = total = quant_produto = produto_caro = produto_barato = nome_prod_barato = 0
while True:
    nome_produto = str(input("Nome do produto:"))
    preco_produto = float(input("Preço do produto:"))
    total += preco_produto
    quant_produto += 1
    if quant_produto == 1:
        produto_barato = preco_produto
        nome_prod_barato = nome_produto
    else:
        if preco_produto <= produto_barato:
            produto_barato = preco_produto
            nome_prod_barato = nome_produto
    if preco_produto >= 1000:
        produto_caro += 1
    resposta_usuario = str(input("Deseja Continuar?")).upper()
    if resposta_usuario == "SIM":
        pass
    elif resposta_usuario == "NAO":
        break
    else:
        break
print('''\nAo todo será gasto R${:.2f} na compra
temos {} produtos que custam R$1000 ou mais
O nome do produto mais barato é {} esse custa R${:.2f}'''.format(total, produto_caro, nome_prod_barato, produto_barato))
print("\nFim do Programa!")
