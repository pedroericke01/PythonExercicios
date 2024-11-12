# script que tem uma tupula com numeros de 0 a 20, escrito por extensso, o programa deverá
# receber a entrada do usuario e verificar se esse numero existe ou não na tupula:#

numeros = ("zero", "um", "dois", 'tres', 'quatro',
           'cinco', 'seis', 'sete', 'oito', 'nove', 'dez',
           'onze', 'doze', 'treze', 'quatorze', 'quinze',
           'dezesseis', 'dezessete', 'dezoito','dezenove', 'vinte')
resposta_usuario = 0
while True:
    escolha_usuario = int(input("Escolha um numero [0/20]:"))
    if 0 <= escolha_usuario <= 20:
        pass
    else:
        print("Tente Novamente!", end=" ")
    resposta_usuario = str(input("Deseja Continuar?[SIM/NAO]")).upper().strip()
    if resposta_usuario == "NAO":
        break
print(f"Você Escolheu o numero {numeros[escolha_usuario]}")
print("Fim")
