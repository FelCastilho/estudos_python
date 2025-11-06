# 🧩 Exercício 3
# Crie uma lista chamada "compras".
# Peça para o usuário digitar 3 produtos (usando input) e adicione-os à lista.
# Depois, exiba a lista completa.

first_product = input("Primeiro produto: ")
second_product = input("Segundo produto: ")
third_product = input("Terceiro produto: ")
fourth_product = input("Quarto produto: ")
fifth_product = input("Quinto produto: ")

products_list = [first_product, second_product, third_product, fourth_product, fifth_product]

print(f"\n\nProdutos adicionados: {products_list[0]},{products_list[1]},{products_list[2]},{products_list[3]},{products_list[4]} \n\nQuantidade total de produtos: {len(products_list)}")