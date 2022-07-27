import math
Ang = float(input("Digite o angulo: "))
seno = math.sin(math.radians(Ang))
cosseno = math.cos(math.radians(Ang))
tangente = math.tan(math.radians(Ang))



print("o angulo de {} tem o seno {:.2f}".format(Ang, seno))
print("o angulo de {} tem o cosseno {:.2f}".format(Ang, cosseno))
print("o angulo de {} tem a tangente {:.2f}".format(Ang, tangente))