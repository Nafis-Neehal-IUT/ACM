#include <iostream>
#include <vector>
#include <numeric>

using namespace std;

int main(){

    int problems, samples, input, start=0, end=3, sample_sum=0, total_count=0;
    vector <int> v;
    cin >> problems;
    samples = problems*3;
    for(int i=0; i<samples; i++){
        cin >> input;
        v.push_back(input);
    }
    while(samples){
        for(int j=start; j<end; j++){
            if(v[j]==1){
                sample_sum++;
            }
        }
        if(sample_sum>=2){
            total_count++;
        }
        sample_sum=0;
        start = end;
        end = end+3;
        samples = samples -3;
    }
    cout << total_count << endl;
    return 0;
}