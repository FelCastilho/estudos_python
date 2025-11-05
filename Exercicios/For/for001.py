# Crie um programa que:
# 1. Peça 5 números ao usuário e salve-os em uma lista.
# 2. Use um loop 'for' para percorrer essa lista.
# 3. Some apenas os números pares.
# 4. No final, mostre:
#    - Todos os números digitados ✅
#    - Somente os pares ✅
#    - E a soma dos pares

first_number = int(input("Primeiro número: "))
second_number = int(input("Primeiro número: "))
third_number = int(input("Primeiro número: "))
fourth_number = int(input("Primeiro número: "))
fifth_number = int(input("Primeiro número: "))

pairs_number = []

numbers_list = [first_number, second_number, third_number, fourth_number, fifth_number]

for number in numbers_list:
    if number % 2 == 0:
        pairs_number.append(number)
        
for pairs in pairs_number:
    sum_pairs += pairs


print(f"\nPrimeiro número: {first_number}\nSegundo número: {second_number}\nTerceiro número: {third_number}\nQuarto número: {fourth_number}\nQuinto número: {fifth_number}\n\nTodos os pares: {pairs_number}\n\nSoma do pares: {sum_pairs}")

