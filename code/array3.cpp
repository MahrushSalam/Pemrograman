#include <iostream>
using namespace std;

int main(){
    char karakter[5] = {'D','$','o','%','8'};

    cout << "isi array pertama :"   << karakter[0] <<endl;
    cout << "isi array pertama :"   << karakter[1] <<endl;
    cout << "isi array pertama :"   << karakter[2] <<endl;
    cout << "isi array pertama :"   << karakter[3] <<endl;
    cout << "isi array pertama :"   << karakter[4] <<endl;

    for (int i = 0; i < 0 ; i++){
        cout << i << " = " << karakter[i] << "\n"; 

    }
    return 0;
}