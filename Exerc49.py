#A série de Fibonacci é formada pela sequência 1,1,2,3,5,8,13,21,34,55,... Faça um algoritmo capaz de gerar a série até o n−ésimo termo.
posicao = int (input("Até qual posicão do fibonacci você quer calcular? "))

termo1 = 1
termo2 = 1
fib = 0

controle = 2
print(termo1, end="\t") 
print(termo2, end="\t")
while(controle < posicao):
    fib = termo1 + termo2
    termo1 = termo2
    termo2 = fib
    print(fib, end="\t")

    controle+=1




