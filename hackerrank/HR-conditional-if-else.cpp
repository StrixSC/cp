// https://www.hackerrank.com/challenges/c-tutorial-conditional-if-else/problem

#include <bits/stdc++.h>
#include <unordered_map>

using namespace std;

int main()
{
    int n;
    cin >> n;
    cin.ignore(numeric_limits<streamsize>::max(), '\n');
    
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
    
    
    // Write Your Code Here

    if (n <= 9 && n > 0) {
        cout << num_map[n] << endl;
    }
    else {
        cout << "Greater than 9" << endl;
    }

    return 0;
}