#include <iostream>
#include <algorithm>
using namespace std;
int main()
{
	int m, h, n, c, b, total=0;
	cin >> m >> h >> n;
	for (int i = 0; i < n; i++)
	{
		cin >> c >> b;
		total += max(m * c, h * b);
	}
	cout << total << "\n";
	return 0;
}