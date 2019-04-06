#include <iostream>
#include <iomanip>

using namespace std;

int main(){

    double R, A, pi = 3.14159;
    cin >> R;
    cout << fixed;
    cout << setprecision(4);
    cout << "A=" << pi * R * R << endl; 
    return 0;
}