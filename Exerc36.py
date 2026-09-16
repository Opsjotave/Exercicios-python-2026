#Faça um algoritmo que leia um número e exiba o dia correspondente da semana. (1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido.
dia = (input("Informe um númrero e veja com qual dia da semana ele é correspondente: "))

if (dia == "1"):
    print ("O ", dia ," é Domingo.")

elif (dia == "2"):
    print ("o", dia, "é Segunda-feira.")

elif (dia == "3"):
    print ("o", dia, "é Terça-feira.")

elif (dia == "4"):
    print ("o", dia, "é Quarta-feira.")

elif (dia == "5"):
    print ("o", dia, " Quinta-feira.")

elif (dia == "6"):
    print ("o", dia, "é Sexta-feira.")

else:
    print ("o", dia, "é Sábado.")
