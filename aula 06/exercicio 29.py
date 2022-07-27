V = int(input("Qual a velocida do seu carro: "))

Valor =  (V-80)*7

if V <= 80:
    print("Você não ultrapassou o limite de velocidade")
else:
    print("="*20,"VOCÊ FOI MULTADO","="*20)
    print("Você terá que pagar um total de R${},00 Reais".format(Valor))

