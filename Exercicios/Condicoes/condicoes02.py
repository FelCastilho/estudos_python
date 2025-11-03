#Crie um programa que simule o login de um site. O usuário deve digitar um nome de usuário e uma senha.

user = input("Digite seu usuário: ")
password = input("Digite sua senha: ")

user_correct = "felipe"
password_correct = "12345"

if user == user_correct and password == password_correct:
    print("Login bem-sucedido!")
elif user == user_correct and password != password_correct:
    print("A senha está incorreta!")
elif user != user_correct and password == password_correct:
    print("O usuário está incorreto!") 
else:
    print("Acesso negado!")
