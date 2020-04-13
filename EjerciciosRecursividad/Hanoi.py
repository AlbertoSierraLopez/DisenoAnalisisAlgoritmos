def hanoi(n, o, d, a):
    if n == 1:
        print("Mover", n, "de", o, "a", d)
    else:
        hanoi(n - 1, o, a, d)
        print("Mover", n, "de", o, "a", d)
        hanoi(n - 1, a, d, o)


hanoi(3, 'O', 'D', 'A')
