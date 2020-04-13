def horner(x, d):
    l = len(d)
    if l == 1:
        return d[0]
    elif l == 2:
        return d[0] + d[1] * x
    else:
        return d[0] + (x * horner(x, d[1:l]))


'''
x = 5
d = [2, 4, 3, 1]
print(horner(x, d))
'''

print("Introduce x:")
n = int(input())

a = []
print("Grado del polinomio:")
grado = int(input())
print("Introduce polinomio:")
for i in range(grado+1):
    o = int(input())
    a.append(o)
print("x:", n, "d:", a)
print("Resultado:")
print(horner(n, a))
