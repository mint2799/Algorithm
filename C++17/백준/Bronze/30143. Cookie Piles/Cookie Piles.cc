#include <iostream>
using namespace std;
int main() {
    int i, n, a, d;
    for (cin >> i; i--;) {
        cin >> n >> a >> d;
        cout << (n * (2 * a + (n - 1) * d)) / 2 << "\n";
    }
    return 0;
}