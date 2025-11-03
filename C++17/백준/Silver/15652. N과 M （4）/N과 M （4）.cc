#include <iostream>
#include <algorithm>
#define MAX 9
using namespace std;

int n, m;
int arr[MAX];

void dfs(int start, int depth);

int main()
{
	cin >> n >> m;
	dfs(1, 0);
	return 0;
}

void dfs(int start, int depth) {
	if (depth == m) {
		for (int i = 0; i < m; i++)
			cout << arr[i] << ' ';
		cout << "\n";
	}
	else {
		for (int i = start; i <= n; i++) {
			arr[depth] = i;
			dfs(i, depth + 1);
		}
	}
}