km = float(input("Quantos km tem sua viagem: "))

if km <= 200:
    print("você terá que pagar um total de R${}".format(km*0.50))
else:
    print("Para viagem acima de 200km, você terá que pagar um total de R${}".format(km*0.45))