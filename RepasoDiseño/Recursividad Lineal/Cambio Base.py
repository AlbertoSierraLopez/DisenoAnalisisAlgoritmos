def Cambio_Base(n, b):
    if n < b:
        return n
    else:
        return Cambio_Base(n // b, b) * 10 + n % b


n = int(input())
b = int(input())
print(Cambio_Base(n, b))
