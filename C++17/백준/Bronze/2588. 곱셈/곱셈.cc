#include <iostream>
using namespace std;
int main() {
    int a, b;
    cin >> a >> b;
    cout << b % 10 * a << "\n" << b / 10 % 10 * a << "\n" << b / 100 * a << "\n" << a * b << "\n";
    return 0;
}