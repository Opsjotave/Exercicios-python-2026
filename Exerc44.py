#(Com estrutura de repetição) Faça um algoritmo que receba dois números inteiros e gere os números inteiros que estão no intervalo compreendido por eles.

n1 = int (input("Digite dois número e veja o intervalo entre eles:"))
n2 = int (input("Digite dois número e veja o intervalo entre eles:"))
if(n1<=n2):
    for n in range (n1+1, n2):
        print(n)
else:
    for n in range (n2+1, n1):
        print(n)