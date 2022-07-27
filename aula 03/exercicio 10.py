din = float(input('Me diga quanto de dinheiro \nque gostaria de gastar em Dolar:'))

dv = din//5.12
rest = din%5.12

print("Você compraria ${} Dolares, e ficaria com R${:.4}".format(dv, rest))
