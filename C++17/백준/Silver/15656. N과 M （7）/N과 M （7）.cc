#include <iostream>
#include <algorithm>
#define MAX 8
using namespace std;

int n, m;
int arr[MAX];
int res[MAX];

void dfs(int depth);

int main()
{
	cin >> n >> m;
	for (int i = 0; i < n; i++)
		cin >> arr[i];
	sort(arr, arr + n);
	dfs(0);
	return 0;
}

void dfs(int depth) {
	if (depth == m) {
		for (int i = 0; i < m; i++)
			cout << res[i] << ' ';
		cout << "\n";
	}
	else {
		for (int i = 0; i < n; i++) {
			res[depth] = arr[i];
			dfs(depth + 1);
		}
	}
}