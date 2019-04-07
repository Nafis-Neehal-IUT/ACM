#include <iostream>
#include <string>
#include <cstring>

using namespace std;

int main(){
    int n, len;
    char first, last;
    string str, num_str, final;
    cin >> n;
    while(n--){
        cin >> str;
        len = str.size();
        if(len<=10){
            cout << str << endl;
        }else{
            first = str[0];
            last = str[len-1];
            num_str = to_string((len-2));
            final = first + num_str + last;
            cout << final << endl;
        }
    }
    return 0;
}