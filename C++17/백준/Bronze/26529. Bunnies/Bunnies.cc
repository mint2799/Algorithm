#include <iostream>
using namespace std;
int n;
int fib[46];
int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);

	fib[0] = fib[1] = 1;
	for (int i = 2; i < 46; i++) fib[i] = fib[i - 1] + fib[i - 2];

	cin >> n;
	while (n--) {
		int x;  cin >> x;
		cout << fib[x] << '\n';
	}
}