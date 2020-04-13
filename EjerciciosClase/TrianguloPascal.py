# Devuelve el piso n del triángulo como lista
def pascal(n):
    if n == 1:
        return [1]
    else:
        return [1] + aux(pascal(n-1)) + [1]


def aux(piso_previo):
    a = []
    for i in range(len(piso_previo)-1):
        a.append(piso_previo[i] + piso_previo[i+1])
    return a


x = int(input())
for j in range(x):
    print(pascal(j+1))
