#include <iostream>
#include <algorithm>
using namespace std;
int main() {
	string s;
	cin >> s;
	string r = s;
	reverse(r.begin(), r.end());
	cout << (r == s ? "1\n" : "0\n");
	return 0;
}