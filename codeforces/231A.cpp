#include <iostream>
using namespace std;

int main() {
    int count;
    int total = 0;
    cin >> count;
    for(int i= 0; i < count; ++i){
        int a,b,c;
        cin >> a >> b >> c;

        if(a + b + c >= 2){
            total++;
        }
    }

    cout << total;
}