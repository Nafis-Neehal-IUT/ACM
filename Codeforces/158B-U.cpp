#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main(){

    int n, input, count=0;
    vector <int> v;
    cin >> n; 
    for(int i=0; i<n; i++){ // O(n)
        cin >> input;
        v.push_back(input);
    }
    sort(v.begin(), v.end(), greater<int>());
    for (int j=0; j<v.size(); j++){ // O(n^2)
        if(v[j]==4){
            count++;
            v[j] = 0;
            continue;
        }
        for (int k=j+1; k<v.size(); k++){
            if(v[j]+v[k]<4){     // if sum < 4
                v[j] = v[j] + v[k];
                v[k] = 0;
            } else if (v[j] + v[k] ==4){    // if sum = 4
                v[j]=0;
                v[k]=0;
                count++;
                break;
            } 
        }
        if(v[j]!=0){    // if nothing matches
            count++;
            v[j]=0;
        }
    }
    cout << count << endl;
    return 0;
}    
    