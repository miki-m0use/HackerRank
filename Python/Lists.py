# Problema: Lists
#
# Considera una lista (list) vacía. Se te darán N comandos. 
# Cada comando será de las siguientes formas:
#
# - insert i e  : Inserta el entero e en la posición i.
# - print       : Imprime la lista.
# - remove e    : Elimina la primera ocurrencia del entero e.
# - append e    : Agrega el entero e al final de la lista.
# - sort        : Ordena la lista.
# - pop         : Elimina el último elemento de la lista.
# - reverse     : Invierte el orden de la lista.
#
# Tu tarea es ejecutar los N comandos en orden y modificar la lista en consecuencia.
#
# Formato de entrada:
# - La primera línea contiene un entero N, el número de comandos.
# - Las siguientes N líneas contienen uno de los comandos mencionados.
#
# Formato de salida:
# - Para cada comando "print", imprime la lista resultante.
#
# Ejemplo de entrada:
# 12
# insert 0 5
# insert 1 10
# insert 0 6
# print
# remove 6
# append 9
# append 1
# sort
# print
# pop
# reverse
# print
#
# Ejemplo de salida:
# [6, 5, 10]
# [1, 5, 9, 10]
# [9, 5, 1]

def main():

    lista = []
    print("Ingrese la cantidad de comandos a ejecutar: ")
    n = int(input())

    print("Ingrese los comandos: ")
    for _ in range(n):
        lineas_comandos = input().split()
        comandos = lineas_comandos[0]
        valores = list(map(int, lineas_comandos[1:]))

        if comandos == "insert":
            lista.insert(valores[0], valores[1])

        elif comandos == "print":
            print(lista)

        elif comandos == "remove":
            lista.remove(valores[0])

        elif comandos == "append":
            lista.append(valores[0])
        elif comandos == "sort":
            lista.sort()
        elif comandos == "pop":
            lista.pop()
        elif comandos == "reverse":
            lista.reverse()


main()