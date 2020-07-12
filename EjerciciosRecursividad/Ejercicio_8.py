def hanoi_variante(n, o, d, a):
    if n == 1:
        print("Mueve disco", n, "desde torre", o, "a torre", a)
        print("Mueve disco", n, "desde torre", a, "a torre", d)
    else:
        hanoi_variante(n - 1, o, d, a)
        print("Mueve disco", n, "desde torre", o, "a torre", a)
        hanoi_variante(n - 1, d, o, a)
        print("Mueve disco", n, "desde torre", a, "a torre", d)
        hanoi_variante(n - 1, o, d, a)


x = int(input())
hanoi_variante(x, '1', '3', '2')    # Origen 1
                                    # Destino 3
                                    # Auxiliar 2
