#include <iostream>
using namespace std;
int main() {
	int t, c, q = 0, d = 0, n =0 , p = 0;
	for (cin >> t; t--;) {
		cin >> c;
		q = c / 25;
		c %= 25;
		d = c / 10;
		c %= 10;
		n = c / 5;
		c %= 5;
		p = c;
		cout << q << " " << d << " " << n << " " << p << endl;
	}
}