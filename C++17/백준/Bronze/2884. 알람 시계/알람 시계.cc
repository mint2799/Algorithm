#include <iostream>
using namespace std;
int main() {
    int h, m;
	cin >> h >> m;
	if (m < 45) {
		h--;
		m += 15;
		if (h < 0) h += 24;
	}
	else m -= 45;
	cout << h << " " << m << "\n";
    return 0;
}