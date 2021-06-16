// https://codeforces.com/problemset/problem/339/A
// StrixSC
#include <iostream>
#include <vector>
#include <sstream>
#include <iterator>
#include <algorithm>

using namespace std;

int main() {
	vector<string> tmp;
	string in;
	cin >> in;

	istringstream iss(in, istringstream::in);
	string s;

	while(getline(iss, s, '+' )) {
		tmp.push_back(s);
	}
	
	sort(tmp.begin(), tmp.end());
	
	string out;
	ostringstream oss(out, ostringstream::out);
	std::copy(tmp.begin(), tmp.end() - 1, std::ostream_iterator<string>(oss, "+"));
	oss << tmp.back();
	
	cout << oss.str() << endl;
}