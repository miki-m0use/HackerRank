
# Dado el registro de puntuaciones de los participantes en el Día Deportivo de la universidad,
# se deben almacenar las puntuaciones en una lista y encontrar la puntuación del subcampeón(la segunda más alta).
# La entrada consiste en dos líneas: la primera contiene un entero n, la cantidad de participantes,
# y la segunda línea contiene n enteros separados por espacios que representan las puntuaciones.


def borrar_duplicados(array, n):
    arrayOrdenado = sorted(array)
    maximo = arrayOrdenado[-1]
    for i in range(n-2, -1, -1):
        if arrayOrdenado[i] != maximo:
            return arrayOrdenado[i]
    return "No hay subcampeon"


l = int(input())
arr = list(map(int, input().split()))

print(borrar_duplicados(arr, l))
