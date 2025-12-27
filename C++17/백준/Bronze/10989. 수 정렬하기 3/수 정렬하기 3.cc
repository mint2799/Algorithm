#include <iostream>
using namespace std;
int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    int n, cnt[10001] = {0};
    cin >> n;
    for (int i = 0; i < n; i++){
        int num;
        cin >> num;
        cnt[num]++;
    }
    for (int i = 0; i <= 10000; i++){
        while (cnt[i]--){
            cout << i << "\n";
        }
    }
}