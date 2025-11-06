# 🧩 Exercício 4 — Versão Avançada e Aplicada (com jogos)
# Você vai criar um pequeno sistema de gerenciamento de jogos.
#
# 1. Crie uma lista chamada "jogos" com 5 nomes de jogos.
# 2. Mostre a lista completa na tela.
# 3. Peça ao usuário que digite o nome de um jogo para remover da lista.
# 4. Antes de remover, verifique com uma condição (if) se o jogo realmente existe na lista:
#    - Se existir, remova e mostre a nova lista atualizada.
#    - Se não existir, exiba uma mensagem dizendo que o jogo não foi encontrado.
# 5. No final, mostre a quantidade total de jogos restantes.

game_list = ["Fallout 4", "Silent hill 2", "Hogwart's legacys", "Dark Souls", "Sekiro"]

print("\nJogos disponíves: \n")

for games in game_list:
    print("*", games)

response = input("\nGostaria de remover algum jogo? (Sim/não)")

if response == "Sim" or response == "sim" or response == "s" or response == "S":
    print("\nQual jogo você gostaria de remover?\n")
    game_name = input()
    
    if game_name in game_list:
        game_list.remove(game_name)
        for games in game_list:
            print("\n*", games)
    else:
        print("\nJogo não encontrado.")

else:
    exit()
    
print(f"\nQuantidade total de jogos: {len(game_list)}")