#include <iostream>
using namespace std;
int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    
    long long vk,jk,vl,jl,vh,dh,jh;
    cin >> vk >> jk >> vl >> jl >> vh >> dh >> jh;
    cout << (vk * jk + vl * jl) * vh * dh * jh;
    return 0;
}