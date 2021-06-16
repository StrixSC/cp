// https://www.hackerrank.com/challenges/c-tutorial-functions/problem
#include <iostream>
#include <cstdio>
#include <algorithm>
#include <vector>
using namespace std;

/*
Add `int max_of_four(int a, int b, int c, int d)` here.
*/
int max_of_four(int const& a, int const& b, int const& c, int const& d) {
    vector<int> tmp = {a, b, c, d};
    return *max_element(tmp.begin(), tmp.end());
}

int main() {
    int a, b, c, d;
    scanf("%d %d %d %d", &a, &b, &c, &d);
    int ans = max_of_four(a, b, c, d);
    printf("%d", ans);
    return 0;
}
