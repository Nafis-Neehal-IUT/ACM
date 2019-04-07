//thanos sort - codeforces 1145A (April Fools Contest 2019)
//Author - Nafis Neehal (nafisneehal.iut@gmail.com)
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

// use g++ <filename.cpp> to compile a c++ file 
//templates
template<typename T>
vector<T> slice(vector<T> const &v, int m, int n){
    auto first = v.cbegin() + m;
    auto last = v.cbegin() + n + 1;
    vector<T> vec(first, last);
    return vec;
}

//search function
int search_max(vector<int> array){
    int result = is_sorted(begin(array), end(array));
    int left_size, right_size; 
    if (result==1){
        return array.size();
    }else{
        int half_array = array.size()/2;
        vector<int> left_vec = slice(array, 0, half_array-1);
        vector<int> right_vec = slice(array, (half_array), array.size()-1);
        left_size = search_max(left_vec);
        right_size = search_max(right_vec);
    }
    return (left_size>right_size) ? left_size: right_size;
}
//main function
int main(){
    int input, len, max;
    vector<int> array;
    cin >> len;
    for (int i=0; i<len; i++){
        cin >> input;
        array.push_back(input);
    }
    max = search_max(array);
    cout << max << endl;
    return 0;
}
