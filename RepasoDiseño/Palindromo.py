def Palindromo(a):
    k = len(a)
    if k == 0:
        return True
    else:
        return a[0] == a[k - 1] and Palindromo(a[1:k - 1])


a = [1, 2, 4, 5, 4, 2, 1]
print(Palindromo(a))
