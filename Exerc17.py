#Faça um algoritmo que receba o salário-base de um funcionário, calcule e mostre o salário a receber, sabendo-se que esse funcionário tem gratificação de 5% sobre o salário-base e paga imposto de 7% sobre o salário-base.
sal= float (input ("Informe seu salário"))

nsal = ((5/100)*sal)+sal

nnsal = nsal-((7/100)*nsal)

print ("seu novo salário é: ", nnsal)