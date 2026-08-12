import time

nome = input("Qual é o teu nome?: ")
idade = int(input("Qual é a tua idade?: "))
vitorias = int(input("Quantas vitórias tens?: "))
vitorias_consecutivas = int(input("Quantas vitórias consecutivas tens?: "))
pontuaçao_atual = int(input("Qual é a tua pontuação atual?: "))
pontuaçao_final = vitorias * 100 + vitorias_consecutivas * 50 + pontuaçao_atual  # calcula a pontuação final multiplicando o número de vitórias pelo valor de cada vitória, somando o número de vitórias consecutivas pelo valor de cada vitória consecutiva e adicionando a pontuação atual.

if pontuaçao_final >= 500:
    print("Estás qualificado!")
else:
    print("Não estás qualificado.")

time.sleep(1)  # pausa de 1 segundo

if pontuaçao_final < 500:
    print("Precisas de mais", 500 - pontuaçao_final, "pontos para te qualificares.")

time.sleep(1)  # pausa de 1 segundo