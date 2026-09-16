#Faça um algoritmo que leia 5 números e informe o maior número.

# n1 = int (input("Digite o 1° número: "))
# n2 = int (input("Digite o 2° número: "))
# n3 = int (input("Digite o 3° número: "))
# n4 = int (input("Digite o 4° número: "))
# n5 = int (input("Digite o 5° número: "))

numeros = []

for n in range(5):
    numeros.append(int (input(f"Digite o {n+1}° número: ")))

print(numeros)
print(max(numeros))
#print(min(numeros))
#print(sum(numeros)/len(numeros))