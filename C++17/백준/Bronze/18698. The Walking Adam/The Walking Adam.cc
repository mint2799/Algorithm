#include <iostream>
#include <string>
using namespace std;

int main() {
    int T;
    cin >> T;

    while (T--) {
        string s;
        cin >> s;

        int steps = s.length();
        for (int i = 0; i < s.length(); i++) {
            if (s[i] == 'D') {
                steps = i;
                break;
            }
        }

        cout << steps << '\n';
    }
    return 0;
}