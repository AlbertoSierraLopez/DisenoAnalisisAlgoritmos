def Quickselect(a, lower, upper, k):  # Selecciona el k-esimo elemento más pequeño de a, si estuviera ordenada, selecciona el elemento que estaría en la posición k
    if lower == upper:
        return a[lower]
    else:
        pivot = Particion_Hoare(a, lower, upper)
        if pivot == k:
            return a[pivot]
        elif pivot > k:
            return Quickselect(a, lower, pivot - 1, k)
        else:
            return Quickselect(a, pivot + 1, upper, k)



###################
def Particion_Hoare(a, lower, upper):
    if upper >= 0:
        middle = (lower + upper) // 2
        pivot = a[middle]
        a[middle] = a[lower]
        a[lower] = pivot

        left = lower + 1
        right = upper

        finished = False
        while not finished:
            while left <= right and a[left] <= pivot:
                left = left + 1

            while a[right] > pivot:
                right = right - 1

            if left < right:
                aux = a[left]
                a[left] = a[right]
                a[right] = aux

            finished = left > right

        a[lower] = a[right]
        a[right] = pivot

        return right
###################