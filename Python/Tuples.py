# Problema: Tuples (HackerRank)
#
# Dado un entero n y una secuencia de n enteros separados por espacios,
# crea una tupla con esos elementos.
#
# Luego, calcula e imprime el valor del hash de esa tupla.
#
# Formato de entrada:
# - La primera línea contiene un entero n, el número de elementos.
# - La segunda línea contiene n enteros separados por espacios.
#
# Formato de salida:
# - Un único entero: el valor de hash de la tupla creada.
#
# Ejemplo de entrada:
# 2
# 1 2
#
# Ejemplo de salida:
# 3713081631934410656


def main():
    print("Ingresa la cantidad de enteros que ingresara")
    n = int(input())
    valores = tuple(map(int, input().split()))

    print(hash(valores))


main()
