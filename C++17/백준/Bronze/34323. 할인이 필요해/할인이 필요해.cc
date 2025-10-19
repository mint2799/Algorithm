#include <iostream>
using namespace std;
int main()
{
	long long n, m, s;
	long long a, b;
	cin >> n >> m >> s;
	a = (100 - n) * s * (m + 1) / 100;
	b = m * s;
	cout << min(a, b) << "\n";
	return 0;
}