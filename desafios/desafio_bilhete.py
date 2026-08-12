print("###############################################\n# Seleciona a tua faixa de idade nesta lista: #\n###############################################")
print()
print(" (1) 6 anos ou menos --> Entrada gratuita")
print(" (2) 7 a 12 anos ------> Bilhete Infantil (6€)")
print(" (3) 13 a 17 anos -----> Bilhete Jovem    (8€)")
print(" (4) 18 anos ou mais --> Bilhete Adulto   (12€)")
print(" (5) 65 anos ou mais --> Entrada gratuita")
print()

idade = input("Seleciona qual a tua faixa de idade (1, 2, 3 ou 4) e pressiona ENTER: ")
print()
if idade == "1":
    print("A tua entrada fica gratuita.")

if idade == "2":
    print("O teu bilhete fica por 6€.")

if idade == "3":
    cartao = input("Tens cartão estudante? (s/n):")
    if cartao == "s":
        print("O teu bilhete fica por 5€.")
    else:
        print("O teu bilhete fica por 8€.")

if idade == "4":
    print("O teu bilhete fica por 12€")

if idade == "5":
    print("A tua entrada fica gratuita.")