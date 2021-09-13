"""
    14. João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar
        o rendimento diário de seu trabalho. Toda vez que ele traz um peso de peixes maior
        que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos)
        deve pagar uma multa de R$ 4,00 por quilo excedente. João precisa que você faça
        um programa que leia a variável peso (peso de peixes) e calcule o excesso. Gravar
        na variável excesso a quantidade de quilos além do limite e na variável multa o
        valor da multa que João deverá pagar. Imprima os dados do programa com as mensagens adequadas.
"""
peso_peixe = int(input("Digite o peso dos peixes pescados: "))
diferenca_peso = peso_peixe - 50
multa = diferenca_peso * 4
if diferenca_peso > 50:
    print(f"O peso excedido da pesca foi: {diferenca_peso}kg")
    print(f"O valor da multa para o excesso é de R${multa}")
else:
    print(f"Peso da pescaria esta dentro do permitido {peso_peixe}kg")
