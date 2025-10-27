#include <iostream>
#include <algorithm>
#define MAX 9
using namespace std;

int n, m;
int arr[MAX];
int res[MAX];
bool visited[MAX];

void dfs(int start, int depth);

int main()
{
	cin >> n >> m; 
	for (int i = 1; i <= n; i++) arr[i-1] = i;
	dfs(1,0);
	return 0;
}

void dfs(int start, int depth) {
	if (depth == m) {
		for (int i = 0; i < m; i++)
			cout << res[i] << ' ';
		cout << "\n";
	}else {
		for (int i = start; i <= n; i++) {
			if (!visited[i]) {
				visited[i] = true;
				res[depth] = arr[i - 1];
				dfs(i + 1, depth + 1);
				visited[i] = false;
			}
		}
	}
}