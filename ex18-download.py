"""
    18.Faça um programa que peça o tamanho de um arquivo para download (em MB) e a
    velocidade de um link de Internet (em Mbps), calcule e informe o tempo aproximado
    de download do arquivo usando este link (em minutos).
"""
arquivo = float(input("Informe o tamanho do arquivo que sera feito o download: "))
velocidade = int(input("Informe a velocidade da internet: "))

tempo = arquivo / (velocidade / 8)
print(f"Tempo em segundos: {tempo:.0f}")
hora = int(tempo / 3600)
resto_hora = tempo % 3600
min = int(resto_hora / 60)
segundos = resto_hora % 60

if hora > 0:
    print(f"Tempo de download {hora}hora(s), {min}min(s) e {segundos:.0f} segundo(s)")
elif 0 < min < 60:
    print(f"Tempo de download {min}min(s) e {segundos:.0f} segundo(s)")
else:
    print(f"Tempo de download {segundos:.0f} segundo(s)")
