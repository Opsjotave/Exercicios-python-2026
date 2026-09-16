#Faça um algoritmo que leia três números e mostre-os em ordem decrescente
num = [None, None, None]

for i in range(3):
    n = int(input(f"Digite o {i+1}º número: "))
    num[i] = n
    print(num)


print(num)

num.sort(reverse=True)

print(num)


# Mostra o resultado na tela
#print("Números em ordem decrescente:", num)
