def NTorres_Wrapper(n):
    # soluciones es una lista de filas, las columnas se codifican como el índice de la lista
    soluciones = [None] * n
    # libres indica las filas en las que una torre todavía no es amenazada
    libres = [True] * n

    NTorres(n, 0, soluciones, libres)


# Es un problema de permutaciones, lo que importa es el orden y cada nodo va a tener n potenciales hijos
def NTorres(n, i, soluciones, libres):
    # Es una solucion completa
    if i == n:
        print(soluciones)
    else:
        # Generar todos los candidatos (la torre puede ir en n filas diferentes)
        for k in range(n):
            # Comprobar que el candidato sea válido
            if libres[k]:
                # Introducir el candidato en la solucion parcial y actualizar la estructura de datos de válidos
                soluciones[i] = k
                libres[k] = False

                # Siguiente nivel en el arbol para introducir más candidatos
                NTorres(n, i + 1, soluciones, libres)

                # Eliminar al candidato de la solucion parcial y restablecer la estructura de datos
                soluciones[i] = None
                libres[k] = True


n = int(input())
NTorres_Wrapper(n)
