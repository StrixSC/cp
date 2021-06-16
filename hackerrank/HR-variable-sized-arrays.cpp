// https://www.hackerrank.com/challenges/variable-sized-arrays/problem
#include <vector>
#include <iostream>

using namespace std;

int main() {
    string ic, qc;
    cin >> ic >> qc;
    vector<vector<string>> all_vectors;
    for(int i = 0; i < stoi(ic); i++) {
        string len;
        cin >> len;
        vector<string> tmp;
        for(int j = 0; j < stoi(len); j++) {
            string elem;
            cin >> elem;
            tmp.push_back(elem);
        }
        all_vectors.push_back(tmp);
    }
    
    for(int i = 0; i < stoi(qc); i++) {
        string ai, ii;
        cin >> ai >> ii;
        cout << all_vectors[stoi(ai)][stoi(ii)] << endl;
    }
}