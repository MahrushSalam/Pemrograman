#include <iostream>
using namespace std;

int main() {
    int n;
    cout << "Jumlah mata kuliah yang diambil : ";
    cin >> n;

    float nilai[n], total = 0, rata;
    float maks, min;

    cout << "Masukkan nilai untuk " << n << " mata kuliah" << endl;

    for (int i = 0; i < n; i++) {
        cout << "Nilai matkul ke-" << i+1 << " : ";
        cin >> nilai[i];
        total += nilai[i];
    }

    maks = nilai[0];
    min  = nilai[0];

    for (int i = 1; i < n; i++) {
        if (nilai[i] > maks) {
            maks = nilai[i];
        }
        if (nilai[i] < min) {
            min = nilai[i];
        }
    }

    rata = total / n;

    cout << "\nOutput program :" << endl;
    cout << "Hasil akhir nilai seluruh mata kuliah" << endl;
    cout << "Rata-rata     = " << rata << endl;
    cout << "Nilai tertinggi = " << maks << endl;
    cout << "Nilai terendah  = " << min << endl;

    if (rata >= 75) {
        cout << "Status LULUS" << endl;
    } else {
        cout << "Status TIDAK LULUS" << endl;
    }

    return 0;
}
