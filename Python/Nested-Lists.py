# Problema: Nested Lists (HackerRank)
#
# Dado los nombres y las notas de N estudiantes, almacénalos en una lista anidada
# y muestra los nombres de los estudiantes que tienen la segunda nota más baja.
#
# Notas:
# - Si hay más de un estudiante con la segunda nota más baja, los nombres deben
#   imprimirse en orden alfabético.
# - Cada nombre debe ir en una nueva línea.
#
# Formato de entrada:
# 1. La primera línea contiene un entero N (el número de estudiantes).
# 2. Las siguientes 2N líneas contienen:
#    - Una línea con el nombre del estudiante.
#    - Una línea con su nota (float).
#
# Restricciones:
# - 2 ≤ N ≤ 5
# - Siempre habrá al menos un estudiante con la segunda nota más baja.
#
# Formato de salida:
# - Los nombres de los estudiantes con la segunda nota más baja,
#   uno por línea, en orden alfabético.
#
# Ejemplo de entrada:
# 5
# Harry
# 37.21
# Berry
# 37.21
# Tina
# 37.2
# Akriti
# 41
# Harsh
# 39
#
# Ejemplo de salida:
# Berry
# Harry



def main():
    lista_notas = []

    cantidad_notas = int(input("Cuantas notas ingresara? : "))

    for _ in range(cantidad_notas):
        nombre = input("Ingrese el nombre del estudiante: ")
        nota = float(input("ingresa la nota del estudiante (numerico): "))
        lista_notas.append([nombre, nota])

    lista_notas = sorted(lista_notas, key=lambda x: x[1])

    solo_notas = sorted(set([nombres[1] for nombres in lista_notas]))

    segunda_nota_mas_baja = solo_notas[1]

    alumnos_segunda = [sub[0] for sub in lista_notas if sub[1] == segunda_nota_mas_baja]

    alumnos_segunda.sort()



    for alumno in alumnos_segunda:
        print(alumno)


main()
