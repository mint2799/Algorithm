#include <iostream>
using namespace std;
int main() {
	int t, x1, y1, floor1, x2, y2, floor2;
	cin >> t;
	for (int i = 0; i < t; i++) {
		cin >> x1 >> y1 >> floor1 >> x2 >> y2 >> floor2;
		int distance = abs(x1 - x2) + abs(y1 - y2) + floor1 + floor2;
		cout << distance << endl;
	}
    return 0;
}