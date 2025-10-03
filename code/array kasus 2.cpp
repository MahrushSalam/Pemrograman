#include <iostream>
using namespace std;

int main() {
    float nilai[10];
    float total = 0;
    float maks, min, rata, selisih;

    for (int i = 0; i < 10; i++) {
        cout << "Nilai ke-" << i+1 << " : ";
        cin >> nilai[i];
        total += nilai[i];
    }

    maks = nilai[0];
    min  = nilai[0];

    for (int i = 1; i < 10; i++) {
        if (nilai[i] > maks) {
            maks = nilai[i];
        }
        if (nilai[i] < min) {
            min = nilai[i];
        }
    }

    rata = total / 10;

    selisih = maks - min;

    cout << "\nOutput program :" << endl;
    cout << "Nilai terbesar = " << maks << endl;
    cout << "Nilai terkecil = " << min << endl;
    cout << "Rata-rata      = " << rata << endl;
    cout << "Selisih        = " << selisih << endl;

    return 0;
}
