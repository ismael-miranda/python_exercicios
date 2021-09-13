"""
    17.Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros
       quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para
       cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00
       ou em galões de 3,6 litros, que custam R$ 25,00.

     ->Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em
       3 situações:
     ->comprar apenas latas de 18 litros;
     ->comprar apenas galões de 3,6 litros;
     ->misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10%
       de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.
"""

area = int(input("Digite, em metros quadrados (m²), a area a ser pintada: "))
litros = (area / 6) * 1.1
print(f'-> Litros de tinta: {litros:.2f}lt')
print()
# considerando latas cheias
print("#Considerando somente latas de 18lt e 3.6lts cheias#")
# galao 18 litros
if litros % 18 == 0:
    galao18 = litros / 18

else:
    galao18 = round((litros / 18) + 0.5)

valor_18 = galao18 * 80
print(f'Galão de 18lt {galao18}: R$ {valor_18:.2f}')

# Galao de 3.6 litros
if litros % 3.6 == 0:
    galao3_6 = litros / 3.6
else:
    galao3_6 = round((litros / 3.6) + 0.5)
valor3_6 = galao3_6 * 25
print(f'Galão de 3.6lt {galao3_6:.0f}: R$ {valor3_6:.2f}')
print()
print("#Misturando latas 18 e latas de 3.6 litros, para ter o menor desperdício#")
resto_galao18 = litros % 18

galao_18 = litros // 18

gal3_6_junto_galao18 = round((resto_galao18 / 3.6) + 0.5)
if galao_18 > 0:
    print(f'Galão de 18lt {galao_18:.0f}')
print(f'Galão de 3.6lt {gal3_6_junto_galao18}')
print("-----------------------------------------")
total = (galao_18 * 80) + (gal3_6_junto_galao18 * 25)
print(f"Total: R$ {total:.2f}")
