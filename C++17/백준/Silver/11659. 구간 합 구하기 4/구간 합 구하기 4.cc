# include <iostream>
using namespace std;
int main() {
	ios::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	int n, m;
	int arr[1000001] = {};
	cin >> n >> m;
	for (int i = 1; i <= n; i++) {
		int tmp;
		cin >> tmp;
		arr[i] = arr[i - 1] + tmp;
	}
	for (int i = 0; i < m; i++) {
		int s, e;
		cin >> s >> e;
		cout << arr[e] - arr[s - 1] << "\n";
	}
	return 0;
}