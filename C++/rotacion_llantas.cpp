#include <iostream>
#include <vector>

using namespace std;

/*
 * Complete the 'calcularFase' function below.
 *
 * The function is expected to return an INTEGER.
 * The function accepts following parameters:
 *  1. STRING pInicial
 *  2. STRING pActual
 */

int calcularFase(string pInicial, string pActual) {

    //soy awenao, pero gracias a mi amigo edicson. Pusheo nuevamente
    string f1 = pInicial;
    string f2 = {pInicial[3], pInicial[2], pInicial[0], pInicial[1]};
    string f3 = {f2[3], f2[2], f2[0], f2[1]};
    string f4 = {f3[3], f3[2], f3[0], f3[1]};
    
    if (pActual == f1) {return 1;}
    else if (pActual == f2) {return 2;}
    else if (pActual == f3) {return 3;}
    else if (pActual == f4) {return 4;}
    
    return -1;
}

int main(){
    string inicial;
    getline(cin, inicial);
    string actual;
    getline(cin, actual);
    
    int resFase = calcularFase(inicial, actual);

    cout << resFase << "\n";
    return 0;
}