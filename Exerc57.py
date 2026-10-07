# (Com estrutura de decisão) Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
# "Telefonou para a vítima?"
# "Esteve no local do crime?"
# "Mora perto da vítima?"
# "Devia para a vítima?"
# "Já trabalhou com a vítima?" 


qtd_resp = 0
resp = ((input ("Telefonou para a vítima?")).upper())[0]
if (resp == "S"):
    qtd_resp = qtd_resp + 1
    
    resp = ((input ("Esteve no local do crime?")).upper())[0]
if (resp == "S"):
    qtd_resp = qtd_resp + 1

    resp = ((input ("Mora perto da vítima?")).upper())[0]
if (resp == "S"):
    qtd_resp = qtd_resp + 1

    resp = ((input ("Devia para a vítima?")).upper())[0]
if (resp == "S"):
    qtd_resp = qtd_resp + 1

    resp = ((input ("Já trabalho copm a vítima?")).upper())[0]
if (resp == "S"):
    qtd_resp = qtd_resp + 1

    if (qtd_resp == 0):
        print ("Você é Inocente ")

    elif (qtd_resp == 1):
        print ("Você é Inocente ")

    elif (qtd_resp == 2):
        print ("Você é suspeito ")
        
    elif (qtd_resp == 3):
        print ("Você é cúmplice")

    elif (qtd_resp == 4):
        print ("Você é cúmplice ")

    elif (qtd_resp == 5):
        print ("Você é assassino ")

    else:
        print("Você não está no caso ")