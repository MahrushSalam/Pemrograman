#include <iostream>
#include <string>
using namespace std;

int main() {
    string kode, namaBarang, bonus;
    int harga = 0, jumlahBeli, subtotal, total;
    char ulang;

    do {
        cout << "Kode Barang : ";
        cin >> kode;

        cout << "Jumlah Beli : ";
        cin >> jumlahBeli;

        if (kode == "IN" || kode == "in") {
            namaBarang = "Indomie";
            harga = 3000;
        } else if (kode == "MG" || kode == "mg") {
            namaBarang = "Minyak Goreng";
            harga = 15000;
        } else if (kode == "GG" || kode == "gg") {
            namaBarang = "Gula";
            harga = 12000;
        } else {
            cout << "Kode barang tidak valid!" << endl;
            continue;
        }

        subtotal = harga * jumlahBeli;

        if (jumlahBeli > 5) {
            bonus = "Tisu";
        } else {
            bonus = "Tidak ada bonus";
        }

        total = subtotal;

        cout << "\nOutput program :" << endl;
        cout << "Nama Barang  : " << namaBarang << endl;
        cout << "Harga        : " << harga << endl;

        cout << "\nJumlah Beli  : " << jumlahBeli << endl;
        cout << "Subtotal     : " << subtotal << endl;
        cout << "Bonus        : " << bonus << endl;
        cout << "Total Belanja: " << total << endl;

        cout << "\nApakah anda akan mengulang? (Y/N) : ";
        cin >> ulang;
        cout << endl;

    } while (ulang == 'Y' || ulang == 'y');

    cout << "Terimakasih telah berbelanja" << endl;

    return 0;
}
