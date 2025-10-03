#include <iostream>
using namespace std;

int main() {
    int n = 5;
    for (int i = 1; i <= n; i++) {
        for (int sp = 0; sp < n - i; sp++) {
            cout << " ";
        }
        for (int j = 0; j < 2*i - 1; j++) {
            cout << "*";
        }
        cout << endl;
    }
    return 0;
}
