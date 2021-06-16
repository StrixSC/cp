// https://codeforces.com/problemset/problem/791/A
// StrixSC
#include <iostream>

using namespace std;

int main() {
	int a, b;
	int x = 0;
	cin >> a >> b;
	while(a <= b) {
		a *= 3;
		b *= 2;
		x++;
	}
	cout << x << endl;
}
