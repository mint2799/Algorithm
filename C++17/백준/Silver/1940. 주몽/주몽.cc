#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;
int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    
    int n, m, cnt = 0;
    cin >> n >> m;
    
    vector<int> arr(n, 0);
    for (int i = 0; i < n; i++)
        cin >> arr[i];
    sort(arr.begin(), arr.end());
    
    int i = 0, j = n-1;
    while (i < j){
        if (arr[i] + arr[j] > m)
            j--;
        else if (arr[i] + arr[j] < m)
            i++;
        else{
            cnt++;
            i++;
            j--;
        }
    }
    cout << cnt << "\n";
}