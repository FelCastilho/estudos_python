# 🧩 Exercício Final — Sistema de Gerenciamento de Estoque (versão sem while)
#
# Objetivo:
# Criar um sistema simples de estoque usando listas, laços e condições.
#
# Etapas:
# 1. Crie uma lista chamada "estoque" vazia.
# 2. Peça ao usuário para digitar o nome de 5 produtos e adicione-os à lista com .append().
# 3. Mostre a lista completa de produtos cadastrados.
# 4. Depois, exiba o menu abaixo e peça para o usuário escolher UMA das opções:
#
#    [1] Adicionar novo produto
#    [2] Remover um produto
#    [3] Listar todos os produtos
#    [4] Procurar um produto específico
#    [5] Sair do sistema
#
# 5. Faça um if/elif/else para tratar cada opção escolhida.
#
#    ✅ [1] → pedir o nome de um novo produto e adicionar ao estoque
#    ✅ [2] → pedir o nome do produto e removê-lo se ele existir
#    ✅ [3] → listar todos os produtos com um laço for
#    ✅ [4] → pedir o nome de um produto e verificar se ele está no estoque
#    ✅ [5] → encerrar o programa
#
# 6. No final, mostre a quantidade total de produtos restantes no estoque.
#
# 💡 Dica:
# Use len(estoque) para contar os produtos
# e o operador "in" para verificar se um produto existe na lista.


# Seu código abaixo 👇


# Pegando os produtos de forma automática (max de 5 produtos)
stock = []

while len(stock) < 5:
    product = input("Digite o nome do produto: ")
    stock.append(product)

print("\nSua lista:\n")

for list_item in stock:
    print("*", list_item)

print ("\nEscolha uma das opções: \n\n[1] Adicionar novo produto\n[2] Remover um produto\n[3] Listar todos os produtos\n[4] Procurar um produto específico\n[5] Sair do sistema\n")

response = int(input(""))

if response > 5 or response < 1:
    print("A opção inserida não existe")
    exit()
elif response == 1:
    print("\nQual o nome do novo produto?\n")
    new_product = input("")
    stock.append(new_product)
    print("\nLista atualizada ✅\n")
    for list_item in stock:
        print("*", list_item)
elif response == 2:
    print("\nDigite o nome do item que será removido\n")
    for list_item in stock:
        print("*", list_item)
    item_for_remove = input("")
    if item_for_remove in stock:
        stock.remove(item_for_remove)
        print("\nLista atualizada ✅\n")
        for list_item in stock:
            print("*", list_item)
    else:
        print("O produto não foi encontrado! ❌")
elif response == 3:
    print("\nProdutos cadastrados:\n")
    for list_item in stock:
        print("*", list_item)
elif response == 4:
    print("\nQual produto gostaria de verificar no estoque?\n")
    product_in_stock = input("")
    
    if product_in_stock in stock:
        print("\nO produto está em estoque ✅")
    else:
        print("\nO produto não está em estoque ❌")
elif response == 5:
    print("\nDesligando sistema...")
    exit()
    
print(f"\nQuantidade de produtos cadastrados: {len(stock)}")
