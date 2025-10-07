#include <iostream>
using namespace std;
int main() {
    int a;
    char grade;
    cin >> a;
	grade = (a >= 90) ? 'A' : (a >= 80) ? 'B' :	(a >= 70) ? 'C' : (a >= 60) ? 'D' : 'F';
	cout << grade << "\n";
    return 0;
}