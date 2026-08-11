moedas = int(input("Quantas moedas tens?: ")) # pergunta ao jogador quantas moedas tem
if moedas >= 10:
    print("#################\n# Podes entrar. #\n#################")
else:
    print("Não tens moedas suficientes. Faltam-te", 10 - moedas, "moedas.")