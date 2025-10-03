#include <iostream>
using namespace std;

int main() {
    double jasa, diskon = 0, potongan, total;

    cout << "Masukkan biaya jasa: ";
    cin >> jasa;

    if (jasa > 500000) {
        diskon = 0.15;
    } else if (jasa > 350000) {
        diskon = 0.125;
    } else if (jasa > 250000) {
        diskon = 0.10;
    } else if (jasa > 150000) {
        diskon = 0.075;
    } else if (jasa > 50000) {
        diskon = 0.05;
    } else {
        diskon = 0.0;
    }

    potongan = jasa * diskon;
    total = jasa - potongan;

    cout << "Total Jasa    : Rp " << jasa << endl;
    cout << "Diskon        : " << diskon * 100 << "%" << endl;
    cout << "Potongan      : Rp " << potongan << endl;
    cout << "Total Bayar   : Rp " << total << endl;

    return 0;
}
