#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    int c;
    vector<int> arr;
    cin >> c;
    
    for (int i = 0; i < c; i++) {
        int t;
        cin >> t;
        arr.push_back(t);   
    }
    
    reverse(arr.begin(), arr.end());
    for(auto i : arr) {
        cout << i << " ";
    }
    return 0;
}
