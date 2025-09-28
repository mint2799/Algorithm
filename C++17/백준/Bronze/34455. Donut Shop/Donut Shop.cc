#include <iostream>
using namespace std;
int main() {
	int d, q, e, res = 0;
	string o;
	cin >> d >> e;
	while (e--) {
		cin >> o >> q;
		res += (o == "+" ? q : -q);
	}
	cout << res + d << "\n";
	return 0;
}