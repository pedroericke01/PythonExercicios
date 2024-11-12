# loop infinito que permite que o usuario digite uma frase e será analisado o numero de
# vogais existentes nessa frase, caso existam, serão impressas para o usuario ver#
# final de toda a manipulação dessa string contida em uma tupula, então será perguntado ao
# usuario se ele deseja ou não continuar com a execucão do sistema, caso sim, a tupula será
# reinicializada desde seu inicio#

resposta_usuario = 0
while True:
    frase = tuple(str(input("Escreva sua frase favorita:")).upper().strip())
    print(f"Na palavra {frase} temos ", end="")
    for caract in frase:
        if caract in "AEIOU":
            print(f"{caract}", end=" ")
    print("Sendo Vogais!\n")
    resposta_usuario = str(input("Deseja Continunar[Sim/Nao]?")).upper().strip()
    while resposta_usuario not in "SIMNAO":
        resposta_usuario = str(input("Deseja Continuar[SIM/NAO]?")).upper().strip()
    if resposta_usuario == "NAO":
        break
print("\nFim")
