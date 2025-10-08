#include <iostream>
using namespace std;
int main() {
    int x, n, a, b, total = 0;
    cin >> x >> n;
    for (int i = 0; i < n; i++) {
        cin >> a >> b;
        total += a * b;
    }
	cout << (total == x ? "Yes" : "No") << "\n";
    return 0;
}