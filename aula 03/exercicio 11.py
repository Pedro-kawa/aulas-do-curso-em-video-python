alt = float(input("Me diga a Altura de sua parede: "))
larg = float(input("Me diga a largura de sua parede: "))

area = alt * larg
l = area / 2

print("A area de sua parede é {}, voce irá precisar de {} litros para pintala.".format(area, l))