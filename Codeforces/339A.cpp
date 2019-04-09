#include <iostream>
#include <string>

using namespace std;

int main(){
    int len; 
    char temp;
    string str;
    cin >> str;
    len = str.size();
    for(int i=0; i<str.size(); i=i+2){
        for(int j=0; j<len; j=j+2){
            if(int(str[j]) > int(str[j+2]) && (j+2)<len){
                temp = str[j];
                str[j] = str[j+2];
                str[j+2] = temp;
            }
        }
        len = len-2;
    }
    cout << str << endl;
    return 0;
}
