#include <iostream>
#include <string>
using namespace std;

int main(){
    int t, x, q;
    double p;
    string item;
    
    cin >> t;
    for(int i=0; i<t; i++){
        double res = 0;
        cin >> x;
        for(int j=0; j<x; j++){
            cin >> item >> q >> p;
            res += q*p;
        }
        cout << fixed;
        cout.precision(2);
        cout << "$" << res << '\n';
    }
}