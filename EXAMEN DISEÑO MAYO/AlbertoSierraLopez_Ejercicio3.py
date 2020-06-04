def permutaciones_con_repeticion(a, n, i, sol_parcial, validos, num_soluciones):
    if i == n:
        print(sol_parcial)              # El programa imprime cada permutación cuando la obtiene
        return num_soluciones + 1       # Y retorna el número de permutaciones calculado cuando termina

    else:
        for k in range(len(a)):
            # El árbol se poda cuando un elemento ya ha excedido su número de apariciones
            if validos[k] > 0:          # ¿Es valido el candidato? ¿O ya se han consumido sus repeticiones?
                validos[k] -= 1         # Se consume una repetición
                sol_parcial[i] = a[k]   # Se inserta el candidato en la solución parcial

                num_soluciones = permutaciones_con_repeticion(a, n, i + 1, sol_parcial, validos, num_soluciones)

                validos[k] += 1         # Se deshacen los cambios para los próximos hijos del árbol de recursión
                sol_parcial[i] = None   # Este cambio es ilustrativo pero no es necesario

    return num_soluciones


def permutaciones_con_repeticion_wrapper(a, r):
    n = sum(r)  # Número de elementos de la permutación
    sol_parcial = [None] * n
    # r va a ser nuestra lista de válidos
    # a será la lista de posibles candidatos
    return permutaciones_con_repeticion(a, n, 0, sol_parcial, r, 0)



a = ['a', 'b', 'c']
r = [ 1,   2,   1 ]
print("Número de permutaciones:", permutaciones_con_repeticion_wrapper(a, r))
