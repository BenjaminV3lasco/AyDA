#Ejercicio 2 Tp 1
def raiz_cuadrada(n):
    # Caso base para n = 0 o n = 1
    if n == 0 or n == 1:
        return n

    # Inicialización de las variables
    x = n  
    y = 0  

    # Iterar hasta que la nueva aproximación de x sea igual a la anterior
    while x != y:
        y = x  # Guardar el valor actual de x
        x = (x + n / x) / 2  # Nueva aproximación utilizando la media de x y n / x
    
    return x  # Aproximación final de la raíz cuadrada

        # Prueba del algoritmo
n = int(input("Ingrese un número entero positivo: "))
resultado = raiz_cuadrada(n)
print(f"La raíz cuadrada aproximada de {n} es: {resultado}")
