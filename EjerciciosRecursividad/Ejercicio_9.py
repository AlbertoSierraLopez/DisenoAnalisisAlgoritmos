def binary_search(a, inf, sup, n):
    mid = (sup + inf) // 2
    if inf > sup:
        return -1
    else:
        if a[mid] == n:
            return mid
        elif a[mid] > n:
            return binary_search(a, inf, mid - 1, n)
        else:
            return binary_search(a, mid + 1, sup, n)


a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
n = int(input())
print(binary_search(a, 0, len(a) - 1, n))
