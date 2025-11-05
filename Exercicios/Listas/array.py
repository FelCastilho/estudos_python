# # 🛒 Exercício — Sistema de Lista de Compras
#
# 1. Peça para o usuário digitar o nome de 5 produtos (um por vez).
# 2. Armazene todos esses produtos em uma lista.
# 3. Mostre:
#    - Todos os produtos adicionados
#    - O primeiro e o último produto da lista
#    - A quantidade total de produtos
# 4. Pergunte se o usuário quer remover algum produto.
#    - Se sim, ele digita o nome do produto e você o remove da lista.
# 5. Mostre a lista atualizada no final.
#
# Dicas:
# - Use .append() para adicionar produtos
# - Use len() para saber a quantidade de produtos
# - Use .remove() para tirar um produto específico
#
# 🚀 Desafio bônus (faça depois de terminar):
#    Adicione um valor para cada produto e mostre o valor total da compra!

# Seu código abaixo 👇

first_product = input("Primeiro produto: ")
second_product = input("Segundo produto: ")
third_product = input("Terceiro produto: ")
fourth_product = input("Quarto produto: ")
fifth_product = input("Quinto produto: ")

products_list = [first_product, second_product, third_product, fourth_product, fifth_product]

print(f"\n\nProdutos adicionados: {products_list[0]},{products_list[1]},{products_list[2]},{products_list[3]},{products_list[4]} \n\nQuantidade total de produtos: {len(products_list)} \n\nDeseja remover algum produto? (Sim / Não)")

response_remove_item = input("")

if response_remove_item == "Sim" or response_remove_item == "sim":
    print("Digite o nome do produto que quer remover:")
    response_how_item = input("")
    
    if response_how_item in products_list:
        products_list.remove(response_how_item)
        print(f"Produto removido com sucesso!\n\nSua lista atualizada: {products_list[0]}, {products_list[1]}, {products_list[2]}, {products_list[3]}")
    else:
        print("O produto não foi encontrado!")
