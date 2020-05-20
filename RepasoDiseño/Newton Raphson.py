def Newton_Raphson(n, a):
    f = (n**2 - a)      # f(n) = n^2 - a ---> n = sqrt(a)
    if abs(f) < 0.00001:
        return n
    else:
        x = n - f/(2*n)
        return Newton_Raphson(x, a)


a = int(input())
print('%.2F' % Newton_Raphson(a, a))
