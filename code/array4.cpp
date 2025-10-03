#include <iostream>
using namespace std;

int main(){
    float angka [] = {1.2, 12.9, -0.55};
    for (int i = 0; i < 3; i++){
    cout << i << " = " << angka[i] << "\n";
    }
    cout << endl;

    angka[0] = 4.00;
    for (int i = 0; i < 3; i++){
    cout << i << " = " << angka[i] << "\n";
    }
    return 0;
}