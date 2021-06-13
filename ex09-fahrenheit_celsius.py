"""
    9.Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura
      em graus Celsius.
"""

fahrenheit = float(input("Digite a temperatura em Fahrenheit: "))
celsius = 5 * ((fahrenheit - 32) / 9)

print(f"{fahrenheit}°F convertidos para Celsius é igual a {celsius:.2f}°C")
