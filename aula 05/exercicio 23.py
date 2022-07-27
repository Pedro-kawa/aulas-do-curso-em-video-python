num = input("Me diga um numero entre 0 a 9999: ")

#maximo 4 caracterias
num = num[0:4]

#Unidades
uni = num[3]
dez = num[2]
cen = num[1]
mil = num[0]

print("""Seu numero {} possue\n{} de unidade\n{} de dezena\n{} de centena
{} de milhar""".format(num, uni, dez, cen, mil))