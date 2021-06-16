// https://codeforces.com/problemset/problem/546/A
// StrixSC
#include <iostream>
#include <vector>

using namespace std;

int main() {
	int k, n, w;
	cin >> k >> n >> w;

	int t = 0;
	for(int i = 0 ; i <= w; i++) {
		t += i * k;
	}
	
	int b = n - t;
	
	cout << (b < 0 ? abs(b) : 0) << endl;

	return 0;
}