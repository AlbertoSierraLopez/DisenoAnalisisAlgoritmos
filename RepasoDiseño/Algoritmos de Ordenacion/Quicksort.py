# In place
def Quicksort(a, lower, upper):
    if lower < upper:
        pivot = Particion_Hoare(a, lower, upper)
        Quicksort(a, lower, pivot - 1)
        Quicksort(a, pivot + 1, upper)


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


a = [6, 4, 1, 7, 4, 7, 3, 6, 5]
print(a)
Quicksort(a, 0, len(a) - 1)
print(a)
