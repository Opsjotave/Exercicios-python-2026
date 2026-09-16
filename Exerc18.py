#Faça um algoritmo que receba o valor de um depósito  e o valor da taxa de juros, calcule e mostre o valor do rendimento e o valor total depois do rendimento.
dep = float (input("Informe o seu depósito:"))
juros = float (input("Informe a taxa de juros:"))

juros = juros/100
rendimento = (dep * juros)
valoratualizado = (rendimento + dep)

print ("Seu valor atualizado é", valoratualizado)