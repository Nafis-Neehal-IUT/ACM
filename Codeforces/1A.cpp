#include <iostream>
#include <cstdlib>

using namespace std;

int main(){

    long long int n,m,a, mul1, mul2;
    cin >> n >> m >> a;
    if(n%a==0){
        mul1 = n/a;
    }else{
        mul1 = n/a + 1;
    }
    if (m%a==0){
        mul2 = m/a;
    }else{
        mul2 = m/a + 1;
    }
    cout << mul1 * mul2 << endl;
    return 0;
}