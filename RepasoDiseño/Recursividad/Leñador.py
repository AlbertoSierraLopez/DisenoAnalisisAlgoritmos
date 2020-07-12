# Esta es la versión básica, se puede hacer con búsqueda binaria
def Woodcutter(t, w, h):
    madera = 0
    for i in t:
        if i > h:
            madera += i - h
    if madera >= w:
        return h
    else:
        return Woodcutter(t, w, h - 1)


def Woodcutter_wrapper(t, w):
    h = max(t) - 1
    return Woodcutter(t, w, h)


t = [5, 4, 3, 12, 8, 7, 5, 10, 7, 8, 4, 4, 11, 8, 7, 1, 9, 4, 3, 5]
print("Arboles:", t)
print("Madera:", end=' ')
w = int(input())
print("Altura:", Woodcutter_wrapper(t, w))
