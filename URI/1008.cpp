#include <iostream>
#include <iomanip>

using namespace std;

int main(){
    int en;
    float hour, per_hour;
    cin >> en >> hour >> per_hour;
    cout << "NUMBER = " << en << endl;
    cout << fixed;
    cout << setprecision(2);
    cout << "SALARY = U$ " << hour * per_hour << endl;
    return 0;
}