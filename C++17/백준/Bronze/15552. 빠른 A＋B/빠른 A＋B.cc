#include <iostream>
using namespace std;
int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    int t, a, b;
    for (cin >> t; t--;) {
        cin >> a >> b;
        cout << a + b << "\n";
    }
    return 0;
}