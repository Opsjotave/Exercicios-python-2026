area = float(input("Digite o tamanho da área em metros quadrados: "))

litros = area / 3

latas = int(litros // 18)
if litros % 18 > 0:
    latas = latas + 1


preco = latas * 80

print("Latas necessárias:", latas)
print("Preço total: R$", preco)
