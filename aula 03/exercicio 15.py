day = float(input("Quantos dias você utilizou o carro?: "))
rodados = float(input("Quantos Km você rodou com o carro?: "))

days = day * 60
km = rodados * 0.15
soma = days + km

print("O valor total a pagar é R${}".format(soma))
