#include <iostream>
#include <vector>
#include <cmath>

using namespace std;

int main(){
    vector <int> v;
    int index, input;
    for(int i=0; i<25; i++){
        cin >> input;
        v.push_back(input);
        if (input==1){
            index = i+1;
        }
    }
    double r = index / 5.00;
    int row = ceil(r);
    int col = index % 5;
    if (col==0){
        col = 5;
    }
    cout << abs(row-3) + abs(col-3) << endl;
    return 0;
}