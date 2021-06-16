// https://codeforces.com/problemset/problem/236/A
// StrixSC
#include <iostream>
#include <vector>
#include <unordered_map>

using namespace std;

int main() {
	string username;
	cin >> username;
	unordered_map<char, int> map;
	
	for(char i : username) {
		if(!map[i]) map[i] = 1;
	}	
	
	int const& size = map.size();
	if(size % 2 == 0) {
		cout << "CHAT WITH HER!" << endl;
	} else cout << "IGNORE HIM!" << endl;
}
