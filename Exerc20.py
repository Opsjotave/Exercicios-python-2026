#Faça um algoritmo que pergunte em que turno você estuda.
#Peça *para digitar M-matutino ou V-Vespertino ou N- Noturno. Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.

letra = ((input("Informe seu turno [M]-Manhã  [V]-Vesperino  [N]-Noturno: ")).upper())[0]
print(letra)
if (letra == "M"):
    print ("Seu período é Matutino. Bom dia!")

elif (letra == "V" or "v"):
    print ("Seu período é Vesperino. Boa Tarde!")

elif (letra == "N" or "n"):
    print ("Seu período é Noturno. Boa Noite!")

else: print ("Informação inválida.")