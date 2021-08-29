"""
    7.Faça um Programa que calcule a área de um quadrado, em seguida mostre o
      dobro desta área para o usuário
"""

lado_quadrado = float(input("Digite um lado do quadrado: "))
area_quadrado = lado_quadrado * lado_quadrado
dobro_area = 2 * area_quadrado

print(f"A área do quadrado é {area_quadrado:.2f}")
print(f"O dobro da area do quadrado é {dobro_area:.2f}")
