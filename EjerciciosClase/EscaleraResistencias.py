def escalera_resistencias(n, r):
    if n == 1:
        return r
    else:
        return ((escalera_resistencias(n - 1, r) + r) + r) / ((escalera_resistencias(n - 1, r) + r) * r)


n = int(input())
r = int(input())
print(escalera_resistencias(n, r))
