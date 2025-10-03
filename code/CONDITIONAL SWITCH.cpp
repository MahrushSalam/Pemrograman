#include <iostream>
using namespace std;

int main (){
    char nilai;

cout << "Input Nilai Anda (A - E): ";
cin >> nilai;   

switch (toupper(nilai))
{
    case 'A':
        cout << "pro player" << endl;
        break;
    case 'B':
        cout << "gg" << endl;
        break;
    case 'C':
        cout << "noob" << endl;
        break;
    case 'D':
        cout << "dc" << endl;
        break;
    case 'E':
        cout << "afk" << endl;
        break;
    default:
        cout << "Maaf, input anda tidak sesuai" << endl;
}
}