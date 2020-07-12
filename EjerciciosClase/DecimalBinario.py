def cambio_base(d):
    # Caso Base
    if d < 2:
        if d == 0:
            return 0
        else:
            return 1
    # Caso Recursivo
    else:
        if d % 2 == 1:
            return 1 + cambio_base(d // 2) * 10
        else:
            return cambio_base(d // 2) * 10


x = int(input())
print(cambio_base(x))
