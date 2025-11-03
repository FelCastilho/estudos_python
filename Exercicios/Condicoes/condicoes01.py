#Crie um programa que leia o peso e a altura de uma pessoa e mostre o IMC junto com uma classificação.

#Fórmula: IMC = peso / (altura ** 2)

# Menor que 18.5 → "Abaixo do peso"
# Entre 18.5 e 24.9 → "Peso normal"
# Entre 25.0 e 29.9 → "Sobrepeso"
# Entre 30.0 e 34.9 → "Obesidade grau 1"
# Entre 35.0 e 39.9 → "Obesidade grau 2"
# 40 ou mais → "Obesidade grau 3"

peso = float(input ("Digite seu peso: "))
altura = float(input ("Digite seu altura: "))

imc  = peso / (altura ** 2)

if imc <= 18.5: 
    print("Abaixo do peso")
elif imc >= 18.5 and imc <= 24.9:
    print("Peso normal")
elif imc >= 25.0 and imc <= 29.9:
    print("Sobrepeso")
elif imc >= 30.0 and imc <= 34.9:
    print("Obesidade grau 1")
elif imc >= 35.0 and imc <= 39.9:
    print("Obesidade grau 2")
elif imc >= 40:
    print("Obesidade grau 3")


