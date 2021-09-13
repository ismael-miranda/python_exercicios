"""
    Faça um programa que pergunte o preço de três produtos e informe qual produto
    você deve comprar, sabendo que a decisão é sempre pelo mais barato.
"""

preco_1 = float(input("Digite o valor do sabonete R$: "))
preco_2 = float(input("Digite o valor do creme dental R$: "))
preco_3 = float(input("Digite o valor do shampoo R$: "))

if preco_2 > preco_1 < preco_3:
    print(f"O produto mais barato é o sabonete R${preco_1}. Comprar o sabonete")
elif preco_1 > preco_2 < preco_3:
    print(f"O produto mais barato é o creme dental R${preco_2}. Comprar o creme dental")
else:
    print(f"O prpduto mais barato é o shampoo R${preco_3}. Comprar o shampoo")
