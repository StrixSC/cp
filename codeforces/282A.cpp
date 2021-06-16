#include <iostream>
using namespace std;

int main() {
    int n;
    cin >> n;
    int x = 0; 
    for(int i = 1; i <= n; ++i) {
        string tmp;
        cin  >> tmp;
        if(tmp == "++X" || tmp == "X++") x++;
        if(tmp == "X--" || tmp == "--X") x--;
    }

    cout << x;
    return 0;
}