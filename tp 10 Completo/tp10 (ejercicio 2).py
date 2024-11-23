def quicksort(arr):
    # Caso base: listas vacías o con un solo elemento ya están ordenadas
    if len(arr) <= 1:
        return arr

    # Elegir el pivote (último elemento de la lista)
    pivot = arr[-1]

    # Dividir la lista en menores, iguales y mayores al pivote
    less = [x for x in arr[:-1] if x <= pivot]
    greater = [x for x in arr[:-1] if x > pivot]

    # Combinar las listas ordenadas con el pivote
    return quicksort(less) + [pivot] + quicksort(greater)

# Lista inicial
unsorted_list = ['E', 'X', 'A', 'M', 'P', 'L', 'E']

# Ordenar la lista usando Quicksort
sorted_list = quicksort(unsorted_list)

print("Lista ordenada:", sorted_list)