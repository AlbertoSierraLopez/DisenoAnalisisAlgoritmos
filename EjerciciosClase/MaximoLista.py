def maximo(a):
    n = len(a)
    if n == 1:
        return a[0]
    else:
        return max(a[n-1], maximo(a[0:n-1]))


a = [3, 1, 6, 5, 9, 7, 2, 8, 4]
print(maximo(a))
