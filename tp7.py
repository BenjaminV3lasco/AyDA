def alternar_vasos(vasos, inicio, fin):
    # Caso base: si el bloque tiene menos de 2 vasos, no hay nada que alternar.
    if fin - inicio <= 1:
        return 0

    # Dividir el problema en dos mitades.
    medio = (inicio + fin) // 2
    movimientos = 0

    # Resolver cada mitad recursivamente.
    movimientos += alternar_vasos(vasos, inicio, medio)
    movimientos += alternar_vasos(vasos, medio, fin)

    # Intercalar vasos llenos y vacíos entre las mitades.
    i, j = inicio, medio
    while i < medio and j < fin:
        if vasos[i] == "lleno" and vasos[j] == "vacío":
            # Intercambiar para alternar.
            vasos[i], vasos[j] = vasos[j], vasos[i]
            movimientos += 1
        i += 1
        j += 1

    return movimientos