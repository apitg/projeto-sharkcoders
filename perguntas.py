username = input("Qual é o nome de utilizador?: ") # pergunta o nome de utilizador

if username == "afonso": # se o nome de utilizador for afonso, então pede a password
    password = input("Qual é a password?: ") # pede a password
    if password == "1234": # se a password for 1234, então...
        print("Bem-vindo, afonso!") # dar boas-vindas
    else:
        print("Password incorreta!") # senão, diz que a password está incorreta
else:
    print("Nome de utilizador incorreto!") # senão, diz que o nome de utilizador está incorreto