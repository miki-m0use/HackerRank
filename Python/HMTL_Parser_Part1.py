# Problema: HTML Parser - Part 1 (HackerRank)
#
# Tu tarea es imprimir todas las etiquetas HTML presentes en un fragmento de código HTML.
# 
# Reglas:
# - Solo imprime los nombres de las etiquetas (sin atributos ni contenido).  
# - Imprime cada etiqueta en la **línea siguiente** a la anterior.
# - El orden debe ser el mismo en que aparecen en el código.
#
# Entrada:
# - Se te da un fragmento de código HTML que puede contener múltiples líneas.
#
# Salida:
# - Cada nombre de etiqueta encontrado debe imprimirse en una línea nueva.
#
# Ejemplo de entrada:
# <html>
# <head>
# <title>Test</title>
# </head>
# <body>
# <h1>Header</h1>
# <p>Paragraph</p>
# </body>
# </html>
#
# Ejemplo de salida:
# html
# head
# title
# head
# body
# h1
# p
# body
# html
#
# Pista:
# - Puedes usar la clase HTMLParser de Python (`from html.parser import HTMLParser`)  
# - Sobrescribe los métodos `handle_starttag` y `handle_endtag` para capturar los nombres de las etiquetas.


def main():
    print("Hello, World!")


main()