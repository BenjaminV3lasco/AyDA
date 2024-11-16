def alternar_discos(fila):
    movimientos = 0
    fila = fila.copy()  # Copia de fila para conservar la original

    for _ in range(len(fila)):
        for i in range(len(fila) - 1):
            if fila[i] == '🔵' and fila[i + 1] == '🔴':
                # Intercambia los discos
                fila[i], fila[i + 1] = fila[i + 1], fila[i]
                movimientos += 1

    return fila, movimientos

n = int(input("Ingrese un número entero positivo: "))
fila_inicial = ['🔴', '🔵'] * n
fila_ordenada, total_movimientos = alternar_discos(fila_inicial)

print("Fila inicial:", "".join(['🔴', '🔵'] * n))
print("Fila ordenada:", "".join(fila_ordenada))
print("Total de movimientos:", total_movimientos)