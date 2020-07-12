def piramide(piso, total):
    if piso > 0:
        piramide(piso - 1, total)
        espacios(total - piso)
        cruces(piso * 2 - 1)
        espacios(total - piso)
        print('')


def espacios(n):
    if n > 0:
        print(' ', end='')
        espacios(n - 1)


def cruces(n):
    if n > 0:
        print('X', end='')
        cruces(n - 1)


x = int(input())
piramide(x, x)
