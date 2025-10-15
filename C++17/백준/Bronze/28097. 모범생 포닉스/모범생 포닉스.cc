#include <iostream>
using namespace std;
int main()
{
	int n, t, h=0;
	cin >> n;
	for (int i = 0; i < n; i++) {
		cin >> t;
		h += t;
	}
	h += (n - 1) * 8;
	cout << (h / 24 > 0 ? h / 24 : 0) << " " << h % 24 << "\n";
	return 0;
}