#include <iostream>
#include <string>
using namespace std;
int main() {
    string type;
    int x;
    int total = 0;

    for(int i = 0; i < 4; i++) {
        cin >> type >> x;
        if(type == "Stair") total += x * 17;
        else if(type == "Es") total += x * 21;
    }
    cout << total << endl;
}