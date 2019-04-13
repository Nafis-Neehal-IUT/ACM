#include <iostream>
#include <vector>

using namespace std;

int main(){
    int stops, input, min_capcity=-1, current_capacity=0;
    cin >> stops;
    for (int i=0; i<stops*2; i++){
        cin >> input;
        if(i%2==0){
            // down
            current_capacity -= input;
        }else{
            //up
            current_capacity += input;
        }
        if(current_capacity>min_capcity){
            min_capcity = current_capacity;
        }
    }
    cout << min_capcity << endl;
    return 0;
}    
    