#include <iostream>
#include <iomanip>

using namespace std;

/*
Theory
--------------------------------------
Average of A and B with weight p and q
(A*p + B*q) / (p+q)
Normal average with p,q = 1 is (A+B)/2
--------------------------------------
*/

int main(){
    float a, b;
    cin >> a >> b;
    cout << fixed;
    cout << setprecision(5);
    cout << "MEDIA = " << (a*3.5+b*7.5)/11 << endl; 
    return 0;
}