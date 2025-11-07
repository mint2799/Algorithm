#include <iostream>
#include <algorithm>
using namespace std;
int main() {
	int n, sum = 0;
	int a[1000];
	int m = a[0];
	cin >> n;
	for (int i = 0; i < n; i++) {
		cin >> a[i];
		m = max(m, a[i]);
	}
	for (int i = 0; i < n; i++) {
		sum += a[i];
	}
	double res = sum * 100.0 / m / n;
	cout << res << "\n";
	return 0;
}