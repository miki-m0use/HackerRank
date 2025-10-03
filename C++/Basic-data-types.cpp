/*
Problema: Basic Data Types (HackerRank)

Tarea:
Declara variables de los siguientes tipos de datos:
- int
- long
- char
- float
- double

Lee de la entrada estándar valores correspondientes a esos tipos de datos, en ese orden, y asígnalos a tus variables.

Después, imprime cada variable en una línea separada en la misma secuencia en que fueron leídas.

Entrada:
- Cinco valores separados por espacios:
  1. Un entero (int)
  2. Un entero largo (long)
  3. Un carácter (char)
  4. Un número de punto flotante (float)
  5. Un número de doble precisión (double)

Salida:
- Imprime cada valor en una nueva línea, en el mismo orden.

Ejemplo de entrada:
3 12345678912345 a 334.23 14049.30493

Ejemplo de salida:
3
12345678912345
a
334.230
14049.304930

Nota:
- Los valores de float y double deben imprimirse con 3 y 9 cifras decimales respectivamente.
- Usa manipuladores de formato (como `fixed` y `setprecision`) para lograrlo.
*/

#include <iostream>
#include <cstdio>
#include <iomanip>

using namespace std;

int main()
{
    int a;
    long long b;
    char c;
    float d;
    double e;

    cin >> a >> b >> c >> d >> e;

    cout << a << endl;
    cout << b << endl;
    cout << c << endl;
    printf("%.3f\n", d);
    printf("%.6f\n", e);

    return 0;
}
