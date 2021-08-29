"""
    15.Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
       Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11%
       para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:

     A.salário bruto.
     B.quanto pagou ao INSS.
     C.quanto pagou ao sindicato.
     D.o salário líquido.
     E.calcule os descontos e o salário líquido, conforme a tabela abaixo:

     + Salário Bruto : R$
     - IR (11%) : R$
     - INSS (8%) : R$
     - Sindicato ( 5%) : R$
     = Salário Liquido : R$

     Obs.: Salário Bruto - Descontos = Salário Líquido.
"""

valor_hora = float(input("Digite o valor hora: "))
horas_trabalhadas = float(input("Digite as horas trabalhadas no mes: "))
sal_bruto = valor_hora * horas_trabalhadas
# desconto IR
des_ir = sal_bruto * 0.11
# desconto INSS
des_inss = sal_bruto * 0.08
# desconto sindicato
des_sind = sal_bruto * 0.05
# total descontos
desconto = des_sind + des_inss + des_sind
# salario Liquido
sal_liq = sal_bruto - desconto

print(f"Salario Bruto......R$ {sal_bruto:.2f}")
print(f"Desconto IR........R$ {des_ir:.2f}")
print(f"Desconto INSS......R$ {des_inss:.2f}")
print(f"Desconto Sindical..R$ {des_sind:.2f}")
print(f"Salario liquido....R$ {sal_liq:.2f}")
