"""
    8.Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
      Calcule e mostre o total do seu salário no referido mês.
"""


valor_hora = float(input("Quanto você ganha por hora: "))
hora_mes = float(input("Quantas horas você trabalha por mes: "))
salario_mes = valor_hora * hora_mes

print(f"O salário desse mes foi de R$ {salario_mes}")
