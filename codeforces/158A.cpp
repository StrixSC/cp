#include <iostream>
using namespace std;

int main() {
    int n,k;
    int total=0;
    int max_score;
    cin >> n >> k;

    for(int i = 1; i <= n; ++i) {
        int tmp;
        cin >> tmp;

        if(tmp == 0) continue;
        if(i == k) max_score = tmp;
        if(i < k || tmp == max_score) total++;
    }

    cout << total;
    return 0;
}
