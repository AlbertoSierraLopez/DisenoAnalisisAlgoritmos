def biseccion(a, b, f, epsilon):    # f() es una función continua en el intervalo (a, b)
    z = (a + b) / 2                 # y tiene un 0 en ese intervalo porque f(a) * f(b) < 0
    if abs(f(z)) < epsilon:
        return z
    elif f(a) * f(z) < 0:
        return biseccion(a, z, f, epsilon)
    else:
        return biseccion(z, b, f, epsilon)


# La función es x^2
def f(x):
    return x * x - 2


print(biseccion(0, 4, f, 10 ** -10))
