"""
    Faça um Programa que verifique se uma letra digitada é vogal ou consoante.
"""
letra = input("Digite uma letra do alfabeto: ")
# vogais = ['a', 'e', 'i', 'o', 'u']

if letra.lower() in "aeiou":
    print("Foi digitado a vogal %s" % letra)
else:
    print("Foi digitado a consoante %s " % letra)
