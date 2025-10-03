#include <iostream>
using namespace std;

int main() {
    int angka[10];
    for (int i = 0; i < 10; i++) {
        cout << "Masukkan bilangan ke-" << i+1 << " : ";
        cin >> angka[i];
    }

    cout << endl;

    cout << "Isi array:" << endl;
    for (int i = 0; i < 10; i++) {
        cout << "bilangan bulat ke-" << i << " = " << angka[i] << endl;
    }

    return 0;
}
