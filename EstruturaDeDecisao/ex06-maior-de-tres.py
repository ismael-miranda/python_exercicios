"""
    Faça um Programa que leia três números e mostre o maior deles.
"""
num1 = int(input("Digite o 1° numero: "))
num2 = int(input("Digite o 2° numero: "))
num3 = int(input("Digite o 3° numero: "))

if num2 < num1 > num3:
    print(f"O 1° numero é o maior. {num1}")
elif num1 < num2 > num3:
    print(f"O 2° numero é o maior. {num2}")
else:
    print(f"O 3° numero é o maior. {num3}")
