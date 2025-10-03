#include <iostream>
using namespace std;

int main() {
    int usia;

    cout << "Masukkan usia pasien: ";
    cin >> usia;

  if (usia <= 5) {
        cout << "ke Dokter Spesialis Bayi." << endl;
    }
    else if (usia <= 16) {
        cout << "ke Dokter Anak." << endl;
    } 
    else if (usia <= 59) {
        cout << "ke Dokter Umum." << endl;
    } 
    else {
        cout << "ke Dokter Geriatri (Spesialis Lansia)." << endl;
    }

    return 0;
}
