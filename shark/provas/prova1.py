import time

espada = 35
escudo = 25
poçao = 7.5
imposto = 0.17

moedas = input("Quantas moedas tens?: ") # pergunta quantas moedas o aventureiro tem
num_poçoes = input("Quantas poções queres comprar?: ") # pergunta quantas poções o aventureiro quer comprar
num_espadas = input("Quantas espadas queres comprar?: ") # pergunta quantas espadas o aventureiro quer comprar
preço_poçoes = int(num_poçoes) * poçao # calcula o preço total das poções
preço_espadas = int(num_espadas) * espada # calcula o preço total das espadas
preço_total = preço_poçoes + preço_espadas + escudo # calcula o preço total da compra
preço_total_com_imposto = preço_total * (1 + imposto) # calcula o preço total com imposto

# calcular quantas moedas sobram
moedas_sobram = float(moedas) - preço_total_com_imposto

# mostrar resumo da compra
print()
print("#################\nResumo da compra:\n#################")
print()
print("Espadas:", int(preço_espadas), "Moedas")
print("Escudo:", escudo, "Moedas")
print("Poções:", int(preço_poçoes), "Moedas")
print("Preço total:", round(preço_total, 2), "Moedas")
print("Preço total com imposto:", round(preço_total_com_imposto, 2), "Moedas")
print("Moedas restantes:", round(moedas_sobram, 2), "Moedas")
print()

time.sleep(1)

# 55 moedas encontradas no chão
print("##############################\nEncontraste 55 moedas no chão!\n##############################")
print()
time.sleep(1)
print("Agora tens", round(moedas_sobram + 55, 2), "Moedas!") # mostra quantas moedas o aventureiro tem agora
print()