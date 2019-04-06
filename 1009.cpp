#include <iostream>
#include <iomanip>

using namespace std;

int main(){
    char name[100];
    float salary, sale;
    cin >> name >> salary >> sale;
    cout << fixed;
    cout << setprecision(2);
    cout << "TOTAL = R$ " << salary + (sale*0.15) << endl;
    return 0;
}