#include <iostream>
using namespace std;
int main()
{
	int t, n;
	for (cin >> t; t--;)
	{
		cin >> n;
		int res = 1;
		for (int i = 1; i <= n; i++)
			res *= i;
		cout << res % 10 << "\n";
	}
	return 0;
}