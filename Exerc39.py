#Faça um algoritmo que leia um número inteiro menor que 1000 e imprima a quantidade de centenas, dezenas e unidades do mesmo. Observando os termos no plural a colocação do "e", da vírgula entre outros. Exemplo:
#326 = 3 centenas, 2 dezenas e 6 unidades 12 = 1 dezena e 2 unidades 
#Testar com: 326, 300, 100, 320, 310,305, 301, 101, 311, 111, 25, 20, 10, 21, 11, 1, 7 e 16
#\(235=(2\times 100)+(3\times 10)+(5\times 1)\)
num = int (input("digite um número e veja as centenas, dezenas e unidades: "))

cent = int(num/100)
print(cent, " centenas,")

dez = int(num/10)
print(dez, " dezenas ")

uni = int(num/1)
print("e ", uni, "unidades.")