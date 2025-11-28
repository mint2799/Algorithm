#include <iostream>
#include <vector>
using namespace std;
int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    
    int n,m,tmp;
    cin >> n >> m;
    vector<long> s(n, 0);
    vector<long> c(m, 0);
    long res = 0;
    cin >> s[0];
    for (int i = 1; i < n; i++){
        cin >> tmp;
        s[i] = s[i-1] + tmp;
    }
    for (int i = 0; i < n; i++){
        int rem = s[i] % m;
        if (rem == 0)
            res++;
        c[rem]++;
    }
    for (int i = 0; i < m; i++){
        if (c[i] > 1)
            res += (c[i] * (c[i] - 1) / 2);
    }
    cout << res << "\n";
    return 0;
}