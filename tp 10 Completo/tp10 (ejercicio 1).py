def merge_sort(arr):
    # Caso base: si la lista tiene un solo elemento o está vacía, ya está ordenada
    if len(arr) <= 1:
        return arr

    # Dividir la lista en dos mitades
    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])

    # Conquistar: fusionar las dos mitades ordenadas
    return merge(left_half, right_half)

def merge(left, right):
    sorted_list = []
    i = j = 0

    # Comparar elementos de ambas mitades y añadirlos en orden
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            sorted_list.append(left[i])
            i += 1
        else:
            sorted_list.append(right[j])
            j += 1

    # Añadir los elementos restantes de ambas mitades (si los hay)
    sorted_list.extend(left[i:])
    sorted_list.extend(right[j:])
    return sorted_list

# Lista inicial
unsorted_list = ['E', 'X', 'A', 'M', 'P', 'L', 'E']

# Ordenar la lista usando MergeSort
sorted_list = merge_sort(unsorted_list)

print("Lista ordenada:", sorted_list)