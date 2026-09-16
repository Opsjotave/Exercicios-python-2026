num1 =int (input("Digite o primeiro número: "))
num2 =int (input("Digite o primeiro número: "))
oper = (input("Informe a operação desejada soma(+) ou subtração (-)"))
resul = (num1 + num2)
resul2 = (num1 - num2)
if (oper == "+"):
  resul = (num1 + num2)
  print("O resultado da sua operação é:", num1 + num2)
  print(f"A soma entre {num1} +  {num2} é {resul}")
else:
 resul2 = (num1 - num2)
 print(f"O resultado da sua operação é:", {num1} - {num2})
 print(f"A subtração entre {num1} - {num2} é= {resul2}")