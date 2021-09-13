"""
    faca um programa que peça  um valor  e mostre se o valor é positivo ou negativo
"""

num = int(input('Informe um numero inteiro positivo ou negativo: '))

if num > 0:
    print(f"O numero informado é positivo ({num})")
else:
    print(f"O numero informado é negativo ({num})")