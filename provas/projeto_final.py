import time

nome = input("Olá! Qual vai ser o teu nome de jogador? ")
print(f"#####################################################\nOlá, {nome}! Bem-vindo ao jogo!\n#####################################################")

time.sleep(1)
print()

print(f"{nome}, agora vais escolher o teu personagem.")
print(" (1) Guerreiro ---> 7 de vida, 10 de ataque, Nenhum poder\n (2) Mago      ---> 15 de vida, 3 de ataque, Regeneração\n (3) Arqueiro  ---> 10 de vida, 7 de ataque, Ataque à Distância")
personagem = input("Escolhe o teu personagem (1, 2 ou 3): ")

vida = 0
ataque = 0
poder = ""

if personagem == "1":
    print("Escolheste o Guerreiro! Ele tem 7 de vida e 10 de ataque! Mas não tem nenhum poder...")
    vida = 7
    ataque = 10
    poder = "Nenhum"
elif personagem == "2":
    print("Escolheste o Mago! Ele tem apenas 3 de ataque, mas 15 de vida, pois consegue regenerar!")
    vida = 15
    ataque = 3
    poder = "Regeneração"
elif personagem == "3":
    print("Escolheste o Arqueiro! Ele tem 10 de vida e 7 de ataque, mas consegue atacar à distância!")
    vida = 10
    ataque = 7
    poder = "Ataque à Distância"
else:
    print("Escolha inválida! Por favor, escolhe 1, 2 ou 3.")
    exit()

time.sleep(8)

print("\n" * 50)

print(f"################################################\nNeste momento, tens {vida} de vida e {ataque} de ataque.")
print(f"O teu poder especial é: {poder}.\n################################################")
time.sleep(7)
print()
moedas = float(100)  # o jogador começa com 100 moedas
print(f"Começas com {moedas} moedas.")
time.sleep(2)
print("Cada aventura custa dinheiro, e no fim de cada aventura, recebes moedas de recompensa.")
time.sleep(2)

print("A tua primeira aventura custa 50 moedas, e vai ser na Floresta Sombria, onde vais procurar por moedas para a próxima aventura, que custa 100 moedas.")
time.sleep(2)
continuar = input("Queres continuar? (s/n): ")

if continuar == "s":
    moedas -= 50
    print()
else:
    print("Adeus!")
    exit()

print("################################################\nA tua primeira aventura vai começar!\n################################################")
time.sleep(2)
continuar_1 = input("Estás a procurar moedas, quando encontras uma moeda rara, que vale 100, mas tem um aspeto estranho. Queres arriscar e apanhar a moeda? (s/n): ")
if continuar_1 == "s":
    print("Era uma armadilha. Morreste.")
    exit()
else:
    print("Escolheste não arriscar. Era uma armadilha.")
    time.sleep(2)
    print(f"Entretanto, encontraste 50 moedas na floresta. Agora tens {moedas} moedas.")
    moedas += 50
    time.sleep(2)

if moedas >= 100 and vida >= 1:
    print(f"Conseguiste sobreviver à primeira aventura! Agora tens {moedas} moedas, e podes ir para a próxima aventura.")
    time.sleep(1)
    print("Ganhaste o jogo. (Por enquanto)")