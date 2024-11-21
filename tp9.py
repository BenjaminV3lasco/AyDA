# Definición de Quickselect: El algoritmo Quickselect es una variante del Quicksort que busca el 𝑘-ésimo elemento más pequeño (o grande) en un arreglo desordenado.

def quickselect(arr, k):
  
    # Validar que k esté dentro del rango del arreglo
    if k < 0 or k >= len(arr):
        raise ValueError("El índice k está fuera del rango del arreglo")
    
    # Inicializar los límites del arreglo
    left = 0
    right = len(arr) - 1
    
    while True:
        # Si el subarreglo tiene solo un elemento, devolverlo
        if left == right:
            return arr[left]
        
        # Seleccionar el pivote (último elemento del subarreglo)
        pivot_index = right
        pivot = arr[pivot_index]
        
        # Realizar la partición del arreglo
        # partition_index será la posición final del pivote
        partition_index = partition(arr, left, right)
        
        # Comparar el índice de partición con k
        if k == partition_index:
            # Si encontramos exactamente el k-ésimo elemento
            return arr[k]
        
        elif k < partition_index:
            # Si k está en el subarreglo izquierdo
            # Reducir el rango de búsqueda a la izquierda
            right = partition_index - 1
        
        else:
            # Si k está en el subarreglo derecho
            # Reducir el rango de búsqueda a la derecha
            left = partition_index + 1

def partition(arr, left, right):

    # Seleccionar el último elemento como pivote
    pivot = arr[right]
    
    # Índice del último elemento menor que el pivote
    store_index = left - 1
    
    # Recorrer el subarreglo
    for j in range(left, right):
        # Si el elemento actual es menor o igual al pivote
        if arr[j] <= pivot:
            # Incrementar el índice de almacenamiento
            store_index += 1
            
            # Intercambiar el elemento actual con el elemento 
            # en el índice de almacenamiento
            arr[store_index], arr[j] = arr[j], arr[store_index]
    
    # Colocar el pivote en su posición final
    arr[store_index + 1], arr[right] = arr[right], arr[store_index + 1]
    
    # Devolver el índice final del pivote
    return store_index + 1

# Ejemplo
if __name__ == "__main__":
    # Ejemplo 1: Encontrar el 3er elemento más pequeño
    arr1 = [7, 10, 4, 3, 20, 15]
    print(f"3er elemento más pequeño: {quickselect(arr1, 2)}")
