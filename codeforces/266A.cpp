// https://codeforces.com/problemset/problem/266/A
// StrixSC
#include <iostream>
#include <sstream>

using namespace std;

int main() {
	int count;
	string in;
	cin >> count >> in;

	char prev;
	int dupes = 0;
	for(char i : in) {
		if (i == prev) {
			dupes++;
		}
		prev = i;
	}

	cout << dupes << endl;
}