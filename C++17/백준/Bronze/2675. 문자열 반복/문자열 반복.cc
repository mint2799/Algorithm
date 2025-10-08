#include <iostream>
using namespace std;
int main() {
	int t, r;
	string s;
	for (cin >> t; t--;) {
		cin >> r >> s;
		for (char c : s) for (int i = 0; i < r; i++) cout << c;
		cout << '\n';
	}
	return 0;
}
