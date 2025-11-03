primeira_nota = float(input("Digite sua primeira nota: "))
segunda_nota = float(input("Digite sua segunda nota: "))

media = (primeira_nota + segunda_nota) / 2

if media >= 7.0: 
    print("Sua média foi:",media, " \nVocê foi aprovado!")
else:
    print("Sua média foi: ", media, " \nVocê foi reprovado!")

