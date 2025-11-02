salario = float (input ("Digite seu salario: "))

if salario <= 2000:
    print ("Junior")
elif salario > 2000 and salario <= 4000:
    print ("Pleno")
elif salario > 4000:
    print ("Senior")