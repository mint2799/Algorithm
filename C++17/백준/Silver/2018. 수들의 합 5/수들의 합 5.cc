#include <iostream>
using namespace std;
int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    
    int n, start=1, end=1, sum=1, cnt=1;
    cin >> n;
    while (end != n){
        if (sum == n){
            cnt++;
            end++;
            sum += end;
        }
        else if (sum > n){
            sum -= start;
            start++;
        }
        else{
            end++;
            sum += end;
        }
    }
    cout << cnt << "\n";
}