#include <iostream>
using namespace std;
int main() {
	int a, b;
	while (1) {
		cin >> a >> b;
		if (a == 0 && b == 0) break;
		cout << ((b % a == 0) ? "factor\n" : ((a % b == 0) ? "multiple\n" : "neither\n"));
	}
	return 0;
}