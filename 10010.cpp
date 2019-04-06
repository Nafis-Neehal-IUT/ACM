#include <iostream>
#include <iomanip>

using namespace std;

int main (){
    int code[2], unit[2];
    float price[2];
    for (int i=0; i<2; i++){
        cin >> code[i] >> unit[i] >> price[i];
    }
    cout << fixed;
    cout << setprecision(2);
    cout << "VALOR A PAGAR: R$ " << unit[0]*price[0] + unit[1]*price[1] << endl;
    return 0;
}