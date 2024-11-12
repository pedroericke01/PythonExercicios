# programa que lê o nome e o preco de vários produtos, o programa deverá perguntar se o
# usuario deseja continuar a inserir outros produtos ou não e no final deverá apresentar:

# 1- O Total gasto na compra
# 2- Quantos produtos custam mais de R$1000
# 3- Nome do Produto mais barato #

print("\n{:=^35}\n".format(" LOJA PESS"))

total = produto_caro = produto_barato = quant_produto = resposta_usuario = 0
while True:
    nome_produto = str(input("Nome do Produto:"))
    preco_produto = float(input("Preço Produto:"))
    total += preco_produto
    quant_produto += 1
    if preco_produto >= 1000:
        produto_caro += 1
    if quant_produto == 1:
        produto_barato = preco_produto
    else:
        if preco_produto <= produto_barato:
            produto_barato = preco_produto
    resposta_usuario = str(input("Deseja Continuar[Sim/Nao]?")).strip().upper()
    while resposta_usuario not in "SIMNAO":
        resposta_usuario = str(input("Deseja Continuar[Sim/Nao]?")).strip().upper()
    if resposta_usuario == "SIM":
        pass
    else:
        break
print(f'''\nO total da compra será {total}
Temos {produto_caro} produto que custam R$1000 ou mais
O produto mais barato custa {produto_barato}''')
print("\nFim do Programa!")
