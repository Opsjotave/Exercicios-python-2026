#Faça um algoritmo que peça um número correspondente a um determinado ano e em seguida informe se este ano é ou não bissexto.
ano = int(input("Digite algum ano e veja se ele é um ano bissexto: "))
if(ano % 4 == 0 ):
    print("O ano", ano, "é bissexto.")
else:
    print("O ano", ano, " não bissexto.")