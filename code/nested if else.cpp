#include <iostream>
using namespace std;
//*note  y untuk ya, n untuk tidak
int main() {
    double total, bayar;
    char sabun, tissue; 
    cout << "Masukkan total belanja: ";
    cin >> total;
    cout << "Apakah ada sabun WANGI? (y/n): ";
    cin >> sabun;
    cout << "Apakah ada tissue HALUS? (y/n): ";
    cin >> tissue;

    if (total > 100000) {
        if (sabun == 'y' || tissue == 'y') {
            bayar = total - (0.10 * total); 
            if (sabun == 'y' && tissue == 'y') {
                bayar -= 5000; 
            }
        } else {
            bayar = total - (0.05 * total); 
        }
    } else {
        bayar = total; 
    }

    cout << "Total yang harus dibayar: Rp " << bayar << endl;
    return 0;
}
