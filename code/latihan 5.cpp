#include <iostream>
using namespace std;

int main () {
    string bulan = "purnama" ;
    if (bulan == "januari") 
    {
        cout << "makan";
    } else if (bulan == "februari")
    {
        cout << "minum";
    } else if (bulan == "maret")
    {
        cout << "ultah";
    } else if (bulan == "april")
    {
       cout << "jalan";
    } else if (bulan == "mei")
    {
        cout << "lari";
    } else if (bulan == "juni")
    {
        cout << "terbang";
    } else if (bulan == "juli")
    {
        cout << "berenang";
    } else if (bulan == "agustus")
    {
        cout << "HUT Indonesia";
    } else if (bulan == "september")
    {
        cout << "tidur";
    } else if (bulan == "oktober")
    {
        cout << "bangun";
    } else if (bulan == "november")
    {
        cout << "sebulan lagi bang";
    } else if (bulan == "desember")
    {
        cout << "Tahun Baru";
    } else {
        cout  << "ini bukan bulan dalam kalender";
    }
    return 0;
}