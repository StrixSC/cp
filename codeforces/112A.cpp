#include <iostream>
#include <ctype.h>
#include <string>

using namespace std;

int main() {
    string a, b;
    cin >> a >> b;

    int atot = 0, btot = 0;

    for(int i = 0; i < a.length(); ++i) {
      a[i] = tolower(a[i], locale());
      b[i] = tolower(b[i], locale());
      atot += (int)a[i];
      btot += (int)b[i];
      if (atot < btot) {
          cout << -1;
          return 0;
      }
      else if (atot > btot) {
         cout << 1;
         return 0;
      }
    }

    cout << 0;
    return 0;
}