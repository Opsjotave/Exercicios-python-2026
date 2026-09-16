nota1 =int (input("Digite sua primeira nota:"))
nota2 =int (input("Digite sua segunda nota:"))
nota3 =int (input("Digite sua terceira nota:"))
nota4 =int (input("Digite sua quarta nota:"))
dis = str (input("Informe sua disciplina:"))
media = (nota1 + nota2 + nota3 + nota4) /4

print ("Sua nota em", dis, "é", media)
if (media >= 7):
    print("Você está aprovado. :)")
else:
    print("Você foi reprovado. :(")