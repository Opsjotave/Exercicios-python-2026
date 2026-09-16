anon = int (input("Digite seu ano de nascimento:"))
anoa = int (input("Digite o ano atual: "))
res = str (input("Já foi do seu aníversario?"))[0].upper()

if (res == "Sim"):
    idadeA = anoa - anon
    idadeM = idadeA*5
    idadeD = idadeA*365.25
    idade2019 = idadeA - 7
    idadeS = idadeD/7
else:
    idadeA = anoa - anon
    idadeM = idadeA*5
    idadeD = idadeA*365.25
    idade2019 = idadeA - 7
    idadeS = idadeD/7

print ("Sua idade é:", idadeA)
print ("Sua idade em meses é:", idadeM)
print ("Sua idade em dias é:", idadeD)
print ("Sua idade em em semanas é:", idadeS)
print ("Sua idade em 2019 era:", idade2019)

