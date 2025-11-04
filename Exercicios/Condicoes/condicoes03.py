#Crie um programa em Python que simule um pequeno sistema de compras, usando apenas condições (if / elif / else).

print ("\nBem vindo a loja! Escolha 3 produtos: \n\n[1] Mouse - R$50.00\n[2] Teclado - R$120.00\n[3] Headset - R$200.00\n[4] Monitor - R$800.00\n[5] Sair sem comprar\n")

first_product = float(input("Primeiro produto: "))
second_product = float(input("Segundo produto: "))
third_product = float(input("Terceiro produto: "))

mouse = 50.00
teclado = 120.00
headset = 200.00
monitor = 800.00

#Capturando o valor dos itens

if first_product == 1:
    first_product = mouse
    first_product_selected = "Mouse"
if second_product == 1: 
    second_product = mouse
    second_product_selected = "Mouse"
if third_product == 1:
    third_product = mouse
    third_product_selected = "Mouse"

if first_product == 2:
    first_product = teclado
    first_product_selected = "Teclado"
if second_product == 2: 
    second_product = teclado
    second_product_selected = "Teclado"
if third_product == 2:
    third_product = teclado
    third_product_selected = "Teclado"

if first_product == 3:
    first_product = headset
    first_product_selected = "Headset"
if second_product == 3: 
    second_product = headset
    second_product_selected = "Headset"
if third_product == 3:
    third_product = headset"
    third_product_selected = "Headset"

if first_product == 4:
    first_product = monitor
    first_product_selected = "Monitor"
if second_product == 4: 
    second_product = monitor
    second_product_selected = "Monitor"
if third_product == 4:
    third_product = monitor
    third_product_selected = "Monitor"
    
if first_product == 5:
    first_product = monitor
    first_product_selected = "Compra cancelada"
    exit()
if second_product == 5: 
    second_product = monitor
    second_product_selected = "Compra cancelada"
    exit()
if third_product == 5:
    third_product = monitor
    third_product_selected = "Compra cancelada"
    exit()

# Soma de cada item

print(f"\nSeu carrinho:\n{first_product_selected}\n{second_product_selected}\n{third_product_selected}\n\nDeseja continuar?\n\n[1] Sim\n[2] Não")

response = int(input(""))

if response == 1: 
    value = first_product + second_product + third_product
    print(f"\nO valor da sua compra é de: R${value:.2f}\nEscolha a forma de pagamento: \n\n[1] Dinheiro / Pix → 10% de desconto\n[2] Cartão à vista → 5% de desconto\n[3] Cartão 2x → preço normal\n[4] Cartão 3x → 20% de juros")
    
    payment_method = int(input(""))
    
    if payment_method == 1:
        final_value = value - (value * 0.10)
        print (f"\nValor com desconto: R${final_value:.2f}")
    elif payment_method == 2:
        final_value = value - (value * 0.05)
        print (f"\nValor com desconto: R${final_value:.2f}")
    elif payment_method == 3:
        final_value = value / 2
        print (f"\nValor total de: R${value:.2f}\nParcelamento em duas vezes sem juros: R${final_value:.2f}")
    elif payment_method == 4:
        final_value = value + (value * 0.20)
        installment_value = final_value / 3
        print (f"\nValor total de: R${value:.2f}\nParcelamento em três vezes com juros de 20%: R${installment_value:.2f}")    

elif response == 2:
    print("Compra cancelada ❌")
    
print("Deseja confirmar a compra?\n\n[1] Sim\n[2] Não")

confirmation = int(input(""))

if confirmation == 1:
    print("Compra confirmada! Obrigado por comprar conosco 😄")
elif confirmation == 2:
    print("Compra cancelada ❌")

