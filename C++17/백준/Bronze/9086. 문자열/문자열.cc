#include <iostream>
#include <cmath>
using namespace std;
int main() {
	int t;
	for (cin >> t; t--;) {
		string s;
		cin >> s;
		cout << s[0] << s[s.length() - 1] << "\n";
	}
	return 0;
}