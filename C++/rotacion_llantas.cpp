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

    int inicio = 0;
    int final = 0;

    //para encontar la fase inicial
    if(pInicial == "ABCD"){
        inicio= 1;
    }else if(pInicial == "DCAB"){
        inicio= 2;
    }else if(pInicial == "BADC"){
        inicio= 3;
    }else if(pInicial == "CDBA"){
        inicio= 4;

    }else{
        return -1;
    }


    //para encontar la fase actual(final)

    if(pActual == "ABCD"){
        final= 1;
    }else if(pActual == "DCAB"){
        final= 2;
    }else if(pActual == "BADC"){
        final= 3;
    }else if(pActual == "CDBA"){
        final= 4;
    }else{
        return -1;
    }

    if(inicio == final){
        return 1;
    }else if(final > inicio){
        return (final - inicio) + 1;
    }else{
        return (4 - inicio) + final + 1;
    }


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