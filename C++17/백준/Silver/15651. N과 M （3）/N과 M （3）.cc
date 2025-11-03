#include <iostream>
#include <algorithm>
#define MAX 9
using namespace std;

int n, m;
int arr[MAX];

void dfs(int depth);

int main()
{
	cin >> n >> m;
	dfs(0);
	return 0;
}

void dfs(int depth) {
	if (depth == m) {
		for (int i = 0; i < m; i++)
			cout << arr[i] << ' ';
		cout << "\n";
	}
	else {
		for (int i = 1; i <= n; i++) {
			arr[depth] = i;
			dfs(depth + 1);
		}
	}
}