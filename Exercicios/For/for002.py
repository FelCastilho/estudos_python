# 🧩 Exercício – Média dos números positivos

# 1. Peça 5 números ao usuário (podem ser positivos ou negativos)
#    - Use int(input()) para cada um.

# 2. Adicione todos os números a uma lista chamada "numbers_list".

# 3. Crie duas variáveis:
#    - sum_positives = 0  (para somar os positivos)
#    - count_positives = 0 (para contar quantos positivos tem)

# 4. Use um loop "for" para percorrer a lista.
#    - Se o número for maior que 0, some ele em sum_positives e incremente count_positives.

# 5. Depois do loop:
#    - Se count_positives for maior que 0, calcule a média.
#    - Caso contrário, mostre "Nenhum número positivo foi digitado."

# 6. Mostre os números positivos e a média formatada com 2 casas decimais.

first_number = int(input("Primeiro número: "))
second_number = int(input("Primeiro número: "))
third_number = int(input("Primeiro número: "))
fourth_number = int(input("Primeiro número: "))
fifth_number = int(input("Primeiro número: "))

numbers_list = [first_number, second_number, third_number, fourth_number, fifth_number]

sum_positives = 0 
count_positives = 0

for n in numbers_list: 
    if n > 0:
        sum_positives += n
        count_positives += 1
        
        
if count_positives > 0:
    media = count_positives / len(n)
    print(f"A média dos números é: {media}")
    print(f"Quantidade de positivos: {count_positives}")
elif:
    print("Nenhum número positivo foi digitado.")
    