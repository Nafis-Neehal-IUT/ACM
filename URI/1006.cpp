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
    float a, b, c;
    cin >> a >> b >> c;
    cout << fixed;
    cout << setprecision(1);
    cout << "MEDIA = " << (a*2+b*3+c*5)/10 << endl; 
    return 0;
}