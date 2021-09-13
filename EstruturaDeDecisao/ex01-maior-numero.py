"""
    Faca um programa que peça dois numeros e imprima o maior valor.
"""

num1 = int(input('Digite o primeiro numero: '))
num2 = int(input('Digite o segunfdo numero: '))

if num1 == num2:
    print(f"Os numeros são iguais.")
elif num1 > num2:
    print(f"O maior numero é {num1}")
else:
    print(f"O maior numero é {num2}")
