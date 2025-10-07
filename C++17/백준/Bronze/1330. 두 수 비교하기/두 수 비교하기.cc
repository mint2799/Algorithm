#include <iostream>
using namespace std;
int main() {
    int a, b;
    string op;
    cin >> a >> b;
    op = a > b ? ">" : a < b ? "<" : a == b ? "==" : "";
    cout << op << "\n";
    return 0;
}