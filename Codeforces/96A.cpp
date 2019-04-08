#include <iostream>
#include <string>

using namespace std;

int main(){
    int len, count=0;
    string str;
    cin >> str;
    for (int i=0; i<str.size(); i++){
        if(str[i+1]==str[i]){
            count++;
        }else{
            count = 0;
        }
        if(count==6){
            break;
        }
    }
    if(count==6){
        cout << "YES" << endl;
    }else{
        cout << "NO" << endl;
    }
    return 0;
}