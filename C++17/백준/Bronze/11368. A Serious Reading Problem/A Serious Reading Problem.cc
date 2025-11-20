#include <iostream>
using namespace std;
int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);
	int C, W, L, P;
	while (cin >> C >> W >> L >> P) {
		if (C == 0) break;
		if (C == 1) cout << 1 << '\n';
		else {
			int ans = 1;
			int rep = W * L * P;
			while (rep--) ans *= C;
			cout << ans << '\n';
		}
	}
}