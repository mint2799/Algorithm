#include <iostream>
using namespace std;
int main() {
    int a, b, c;
    cin >> a >> b >> c;
	a = (a + (b + c) / 60) % 24;
	b = (b + c) % 60;
    cout << a << " " << b << "\n";
    return 0;
}