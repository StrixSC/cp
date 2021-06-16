// https://codeforces.com/contest/263/problem/A
// StrixSC
#include <iostream>
#include <vector>

using namespace std;

int main() {
	int x, y;
	for (int i = 0; i < 5; i++) {
		for(int j = 0; j < 5; j++) {
			int input;
			cin >> input;
			if(input == 1) {
				x = i; y=j;
				break;
			}
		}
	}
	cout << abs(2-x) + abs(2-y);
}