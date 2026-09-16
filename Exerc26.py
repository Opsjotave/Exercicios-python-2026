#Faça um algoritmo que receba dois números maiores que zero, calcule e mostre um elevado ao outro. O expoente deverá ser no máximo 10.

n1 = int (input("Digite o primeiro númrero(<0): "))
n2 = int (input("Digite o primeiro númrero(<0): "))

n1e = n1**n2
n2e = n2**n1

print ("O ", n1, "elevado á", n2, "é", n1e)
print ("O ", n2, "elevado á", n1, "é", n2e)