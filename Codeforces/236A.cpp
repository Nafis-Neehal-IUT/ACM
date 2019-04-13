#include <iostream>
#include <vector>
#include <string>

using namespace std;

int main(){
    string str;
    int count=0;
    int array[26]={0};

    cin >> str;
    for(int i=0; i<str.size(); i++){
        int ascii_num = int(str[i]) - 97;
        if(array[ascii_num]==0){
            count++;
        }
        array[ascii_num]++; 
    }
    if(count%2==0){
        cout << "CHAT WITH HER!" << endl;
    }else{
        cout << "IGNORE HIM!" << endl;
    }
    return 0;
}    
    