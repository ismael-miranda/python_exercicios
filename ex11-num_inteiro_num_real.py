"""
    11.Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:

        A.o produto do dobro do primeiro com metade do segundo .
        B.a soma do triplo do primeiro com o terceiro.
        C.o terceiro elevado ao cubo.
"""

num1 = int(input("Digite um numero inteiro: "))
num2 = int(input("Digite outro numero inteiro: "))
num3 = float(input("Digite um numero real: "))

produto = (num1 * num1) + (num2 / 2)
soma_triplo_mais_terceiro = (num1 * 3) + num3
elevado_cubo = num3 ** 3

print(f"O produto do dobro do primeiro com metade do segundo: {produto}")
print(f"A soma do triplo do primeiro com o terceiro: {soma_triplo_mais_terceiro:.2f}")
print(f"O terceiro elevado ao cubo: {elevado_cubo:.2f}")
