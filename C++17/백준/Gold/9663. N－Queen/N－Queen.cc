#include <iostream>
using namespace std;
int n, cnt;
int col[16];
bool promising(int i) {
	for (int k = 1; k < i; k++) {
		if (col[k] == col[i] || abs(col[i] - col[k]) == abs(i - k))
			return false;
	}
	return true;
}
void Queens(int i) {
	if (promising(i)) {
		if (i == n)
			cnt++;
		else {
			for (int j = 1; j < n + 1; j++) {
				col[i + 1] = j;
				Queens(i + 1);
			}
		}
	}
}
int main() {
	cin >> n;
	cnt = 0;
	Queens(0);
	cout << cnt << "\n";
	return 0;
}