// https://www.hackerrank.com/challenges/c-tutorial-for-loop/problem?h_r=next-challenge&h_v=zen
#include <iostream>
#include <cstdio>
#include <unordered_map>
using namespace std;

int main() {
    // Complete the code.
    int a, b;
    
    cin >> a >> b;
    
    unordered_map<int, string> num_map;
    num_map[0] = "zero";
    num_map[1] = "one";
    num_map[2] = "two";
    num_map[3] = "three";
    num_map[4] = "four";
    num_map[5] = "five";
    num_map[6] = "six";
    num_map[7] = "seven";
    num_map[8] = "eight";
    num_map[9] = "nine";
    
    for(int n = a; n <= b; n++) {
        if(n >= 1 && n <= 9) {
            cout << num_map[n] << endl;
        }
        else if (n > 9 && n % 2 == 0) {
           cout << "even" << endl; 
        }
        else cout << "odd" << endl;
    }
    return 0;
