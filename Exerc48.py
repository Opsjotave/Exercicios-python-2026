
pares = 0
impares = 0

for i in range(10):
    numero = int(input(f"Digite o {i+1}º número inteiro: "))
    
    # Verifica se o resto da divisão por 2 é zero (número par)
    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1

# Mostra o resultado final
print(f"\nQuantidade de números pares: {pares}")
print(f"Quantidade de números ímpares: {impares}")
