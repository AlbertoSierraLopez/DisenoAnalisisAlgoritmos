def reloj(n, o, d, a):
    if n > 0:
        antireloj(n - 1, o, a, d)
        print("Mover", n, "de", o, "a", d)
        antireloj(n - 1, a, d, o)


def antireloj(n, o, d, a):
    if n > 0:
        antireloj(n - 1, o, d, a)
        print("Mover", n, "de", o, "a", a)
        reloj(n - 1, d, o, a)
        print("Mover", n, "de", a, "a", d)
        antireloj(n - 1, o, d, a)


x = int(input())
reloj(x, 'A', 'C', 'B')
