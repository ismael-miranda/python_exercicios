"""
    16.Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados
       da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados
       e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades
       de latas de tinta a serem compradas e o preço total.

"""

area = int(input("Digite, em metros quadrados (m²), a area a ser pintada: "))
litros = area / 3
lata18 = litros / 18

if litros % 18 == 0:
    lata18 = litros / 18
else:
    lata18  = round(lata18+0.5)

valor = lata18 * 80
print(f"Quantidade de latas {lata18}")
print(f"Valor total {valor}")
