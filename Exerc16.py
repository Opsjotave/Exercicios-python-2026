#percentual de aumento, calcule e mostre o valor de aumento e o novo salário.

sal = float(input ("informe seu salário: "))

por = float (input("informe a porcentagem do seu aumento: "))

aum = (por/100)*sal
novosal = sal + aum

print ("Seu salário com o aumento é:", novosal)