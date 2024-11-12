# script que lê o Genero de uma pessoa, caso o genero seja diferente de
# masculino ou feminino o programa vai exigir que seja inserido um valor correto

genero = str(input("Qual é o seu Genero[MASCULINO/FEMININO]?")).strip().upper()
while genero not in "MASCULINOFEMININO":
    genero = str(input("Qual é o seu genero[MASCULINNO/FEMININO]?")).strip().upper()
print(f"\nParabens, seu genero é {genero}")
print("\nFim do Programa!")
