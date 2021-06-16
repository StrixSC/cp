#include <iostream>
#include <string>

using namespace std;

int main() {
    
    int ntc;
    cin >> ntc;

    for(int i = 0; i < ntc; ++i) {
        string a;
        cin >> a;
        int a_count = 0;
        int b_count = 0;
        int c_count = 0;
        cout << endl;
        for(int j = 0; j < a.size(); j++) {
            if(a[j] == 'A') a_count++;
            else if(a[j] == 'B') b_count++;
            else if(a[j] == 'C') c_count++;
        }
        
        cout << a_count << b_count << c_count;
        if(
            ((a_count == b_count) && (c_count == 0)) ||
            ((a_count > b_count) && ((a_count - b_count) == c_count)) ||
            ((a_count < b_count) && ((b_count - a_count) == c_count))
         ) {
            cout << "YES";
        } else cout << "NO";
    }

    return 0;
}