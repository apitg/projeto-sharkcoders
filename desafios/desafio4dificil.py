moedas = int(input("Quantas moedas tens?: "))
vida = int(input("Quantos pontos de vida tens?: "))
nivel = int(input("Qual é o teu nível?: "))
chave = input("Tens a chave? (y/n): ")

if moedas >= 50 and vida >= 30 and nivel >= 5 and chave == "y":
    print("Podes entrar na dungeon!")
else:
    print("Não podes entrar na dungeon!")
    print("Faltam-te algumas coisas:")
    if moedas < 50:
        print("- Moedas: precisas de mais", 50 - moedas, "moedas.")
    if vida < 30:
        print("- Pontos de vida: precisas de mais", 30 - vida, "pontos de vida.")
    if nivel < 5:
        print("- Nível: precisas de pelo menos nível 5. Tens nível", nivel)
    if chave != "y":
        print("- Chave: precisas da chave.")