"""
    Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a
    letra escrever: F - Feminino, M - Masculino, Sexo Inválido.
"""

info_genero = input("Digite F ou M : ").upper()

if info_genero == "F":
    print(f"A letra digitada foi F. Neste script, F é igual a feminino")
elif info_genero == "M":
    print(f"A letra digitada foi M. Neste script, F é igual a masculino")
else:
    print(f"Letra sem atribuição.")
