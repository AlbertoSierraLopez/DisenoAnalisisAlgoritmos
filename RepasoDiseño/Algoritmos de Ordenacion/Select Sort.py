def Select_Sort(a):
    k = len(a)
    if k == 0:
        return a
    else:
        b = list(a)
        m = min(b)
        b.remove(m)
        return [m] + Select_Sort(b)


a = [3, 6, 4, 8, 9, 1, 0, 2, 5, 7]
print(Select_Sort(a))
print(a)