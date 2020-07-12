# Ejercicio 4.6 del libro
def g(m, n, f):
    if m == n:
        return f(m)
    else:
        return f(m) + g(m + 1, n, f)


def f(i):
    return i * i * i


m = int(input())
n = int(input())
print(g(m, n, f))
