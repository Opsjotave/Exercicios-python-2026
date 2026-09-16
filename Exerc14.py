#Faça um algoritmo que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino ou Sexo Inválido.
sexo = str (input("Digite seu sexo (F) (M):"))

if (sexo == "F"):
    print ("Seu sexo é feminino")
elif (sexo == "M"):
    print ("seu sexo é masculino.")
else:
    print ("Sexo não existente, tente novamente.")