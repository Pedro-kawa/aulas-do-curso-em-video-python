ano = int(input("Em que ano você está: "))

Bis = ano % 2

if Bis == 0:
    print("O ano que você está, é bissexto")
else:
    print("O ano que você está, não é bissexto")