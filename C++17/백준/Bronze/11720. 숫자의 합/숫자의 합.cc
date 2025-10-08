#include <iostream>
using namespace std;
int main() {
	int n, res = 0;
	string nums;
	cin >> n >> nums;
	for (int i = 0; i < n; i++)
		res += nums[i] - '0';
	cout << res << "\n";
	return 0;
}