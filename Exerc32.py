#Faça um algoritmo que peça a temperatura em graus Celsius, transforme e mostre a temperatura em graus Fahrenheit e Kelvin.
#Fahrenheit → (0 °C × 9/5) + 32 = 32 °F (EUA e Inglaterra)
#Kelvin → 0 °C + 273,15 = 273,15 K (Química e Física)

graus = float (input("Quantos graus está fazendo hoje?"))

fah = (graus * 9/5) + 32
print ("A temperatura em Fahrenheit é ", fah)

kel = graus + 273,15
print ("A temperatura em Kelvin é", kel)
