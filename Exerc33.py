#Faça um algoritmo que peça 2 números inteiros e um número real. Calcule e mostre:
#o produto do dobro do primeiro com metade do segundo .
#a soma do triplo do primeiro com o segundo.
#o segundo elevado ao cubo.

n1 = int (input("Informe o primeiro número inteiro: "))
n2 = int  (input("informe o segundo número inteiro: "))
n3 = float (input("Informe um número real:"))


produto = (2 * n1) * (n2 / 2.0)
soma = (3 * n1) + n2 
cubo = n2 * n2 * n2

print ("o produto do dobro do primeiro com metade do segundo. ", produto)
print ("a soma do triplo do primeiro com o segundo.", soma)
print ("o segundo elevado ao cubo.", soma)