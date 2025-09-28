# Problema: Finding the Percentage
#
# El usuario recibe un número entero n, el número de estudiantes.
# Después, en las siguientes n líneas, cada línea contiene:
# - El nombre de un estudiante.
# - Sus calificaciones en forma de tres números separados por espacio (floats).
#
# Esos datos deben almacenarse en una estructura adecuada (por ejemplo, un diccionario).
#
# Luego, se recibe una cadena con el nombre de un estudiante.
# El objetivo es imprimir el promedio de las calificaciones de ese estudiante,
# mostrando el resultado con exactamente 2 decimales.
#
# Formato de entrada:
# - La primera línea contiene un entero n, número de estudiantes.
# - Las siguientes n líneas contienen:
#     nombre nota1 nota2 nota3
# - La última línea contiene el nombre de un estudiante.
#
# Formato de salida:
# - Imprimir el promedio de las notas del estudiante consultado,
#   con 2 decimales de precisión.
#
# Ejemplo de entrada:
# 3
# Krishna 67 68 69
# Arjun 70 98 63
# Malika 52 56 60
# Malika
#
# Ejemplo de salida:
# 56.00


def main():
    notas_estudiante = {} #esto es un diccionario
    print("Ingrese la cantidad de estudiantes: ")
    n = int(input())

    print("Ingrese el nombre y las 3 notas de cada estudiante: ")
    for _ in range(n):
        datos = input().split()
        nombre = datos[0]
        notas = list(map(float, datos[1:]))

        notas_estudiante[nombre] = notas


    print("Ingrese el nombre del estudiante para calcular su promedio: ")
    estudiante = input()

    if estudiante in notas_estudiante:
        notas = notas_estudiante[estudiante]
        promedio = sum(notas)/3
        print(f"{promedio:.2f}")
        return 0
    
    print("el estudiante no existe")
    return 0



main()
