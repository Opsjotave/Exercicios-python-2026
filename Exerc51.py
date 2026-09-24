#Faça um algoritmo que peça um número inteiro e determine se ele é ou não um número primo. Um número primo é aquele que é divisível somente por ele mesmo e por 1.
num = int (input("Digite o número e veja se ele é primo: "))
primo = True

if num <= 1:
    primo = False
else:
    for i in range(2, num):
          if num % 1 == 0:
               primo = False

if primo:
     print ("É primo")
else:
     print("Não é primo")               
