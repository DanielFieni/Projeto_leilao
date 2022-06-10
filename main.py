from replit import clear

def definirMaior(nome_dict):
    maior = 0
    vencedor = ""
    for apostador in nome_dict:
        if nome_dict[apostador] > maior:
            maior = nome_dict[apostador]
            vencedor = apostador
    print("Apostas finalizadas")
    print(f"A aposta vencedora foi de {vencedor}\nValor da aposta: R${maior}")

nome_dict = {}
print("Bem vindo ao Leilão")
continuar = True

while continuar:
    nome = str(input("Qual o seu nome: "))
    aposta = float(input("Qual a sua aposta: "))
    nome_dict[nome] = aposta
    continuar = str(input("Deseja continuar: ")).upper()
    clear()
    if continuar != "S":
        continuar = False
        definirMaior(nome_dict)
