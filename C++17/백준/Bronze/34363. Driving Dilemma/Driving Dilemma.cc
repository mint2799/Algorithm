#include <iostream> 
using namespace std;

int main() 
{
    std::ios::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
    
    int S;
    double D, T;
    cin >> S >> D >> T;

    double speed_fps = S * 5280.0 / 3600.0;
    double distance_traveled = speed_fps * T;
    cout << ((distance_traveled >= D) ? "MADE IT\n" : "FAILED TEST\n");
    return 0;
}