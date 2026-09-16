#Faça um algoritmo  que calcule seu peso ideal, para isso receba a altura (h) de uma pessoa, receba o sexo (H para Homens e M para Mulher) e utilize as seguintes fórmulas:
#Para homens: (72.7*h) - 58
#Para mulheres: (62.1*h) - 44.7
h = float (input("Informe sua altura e descubra seu peso: "))
sexo = input(("Qual é seu sexo? ")).upper()

if (sexo == "H"):
    pi= (72.7*h) - 58
    print ("Seu peso ideal é; ", pi)
elif (sexo=="M"):
    pi = (62.1*h) - 44.7
    print("Seu peso ideal é: ", pi)

else: 
    print ("sexo bostaaaaaaaaaaaaaaa")