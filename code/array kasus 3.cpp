#include <iostream>
using namespace std;

int main() {
    int bilangan;
    char ulang;

    do {
        cout << "Input bilangan : ";
        cin >> bilangan;

        bool prima = true;

        if (bilangan <= 1) {
            prima = false;
        } else {
            for (int i = 2; i <= bilangan / 2; i++) {
                if (bilangan % i == 0) {
                    prima = false;
                    break;
                }
            }
        }

        if (prima)
            cout << bilangan << " adalah bilangan prima" << endl;
        else
            cout << bilangan << " bukan bilangan prima" << endl;

        cout << "Apakah anda akan mengulang? (Y/N) : ";
        cin >> ulang;

        cout << endl;

    } while (ulang == 'Y' || ulang == 'y');

    cout << "Program berakhir." << endl;
    return 0;
}
