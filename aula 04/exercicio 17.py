from re import A


from math import sqrt
ctopt = float(input("Me diga o Cateto oposto em cm: "))
ctdj = float(input("Me diga o Cateto adjacent em cm: "))

Pitagoras = ctdj**2 + ctopt**2
a = (sqrt(Pitagoras ))

altura= (ctdj*ctopt)/a






print("O valor da hipotenusa é {} e sua altura é {}".format(a, altura))