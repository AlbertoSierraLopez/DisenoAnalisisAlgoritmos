def capicua(s):
    if len(s) <= 1:
        return True
    elif s[0] == s[len(s) - 1]:
        return capicua(s[1:len(s)-1])
    else:
        return False


def capicua_mas_larga(s):
    if capicua(s):
        return s
    else:
        a = s[0:len(s)-1]
        b = s[1:len(s)]
        if len(capicua_mas_larga(a)) > len(capicua_mas_larga(b)):
            return capicua_mas_larga(a)
        else:
            return capicua_mas_larga(b)


a = ['c', 'b', 'c', 'a', 'b', 'c', 'b', 'a']
print(capicua_mas_larga(a))
