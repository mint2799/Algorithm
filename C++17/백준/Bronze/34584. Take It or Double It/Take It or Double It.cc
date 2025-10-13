#include <iostream>
using namespace std;
int main() {
    long long x, d;
    cin >> x >> d;
    if (2 * x > d)
        cout << "take it\n";
    else
        cout << "double it\n";
    return 0;
}
