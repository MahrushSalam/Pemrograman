#include <iostream>
using namespace std;

int main() {
    string bulan;

    cout << "Masukkan nama bulan: ";
    cin >> bulan;

    if (bulan == "januari") {
        cout << "makan";
    } else if (bulan == "februari") {
        cout << "minum";
    } else if (bulan == "maret") {
        cout << "ultah";
    } else if (bulan == "april") {
        cout << "jalan";
    } else if (bulan == "mei") {
        cout << "lari";
    } else if (bulan == "juni") {
        cout << "terbang";
    } else if (bulan == "juli") {
        cout << "berenang";
    } else if (bulan == "agustus") {
        cout << "HUT Indonesia";
    } else if (bulan == "september") {
        cout << "tidur";
    } else if (bulan == "oktober") {
        cout << "belajar";
    } else if (bulan == "november"){
        cout << "sebulan lagi";
    } else if (bulan == "desember"){
        cout << "tahun baru";
    }
     else {
        cout << "Ini bukan bulan dalam kalender!";
    }

    return 0;
}
