def Subcadena_Palindromo(a):
    k = len(a)
    if Es_Palindromo(a):
        return a
    else:
        a1 = Subcadena_Palindromo(a[1:])
        a2 = Subcadena_Palindromo(a[:k - 1])
        if len(a1) > len(a2):
            return a1
        else:
            return a2


def Es_Palindromo(a):
    k = len(a)
    if k == 0:
        return True
    elif a[0] == a[k - 1]:
        return Es_Palindromo(a[1:k - 1])
    else:
        return False


a = [1, 2, 6, 3, 4, 3, 6, 9, 0, 9, 6, 1]
print(Subcadena_Palindromo(a))
