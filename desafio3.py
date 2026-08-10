# o programa pergunta ao utilizador quantas moedas tem, a seguir perguna qual o preço de uma espada, depois pergunta pelo preço de uma poção, e no fim calcula o que sobra ao utilizador

moedas = int(input("Quantas moedas tens? (normal: 50 moedas): "))
custo_espada = int(input("Quanto custa uma espada?: "))
custo_poçao = int(input("Quanto custa uma poção?: "))

moedas_totais = moedas-custo_espada-custo_poçao
print("Dinheiro de sobra:", moedas_totais,"moedas")