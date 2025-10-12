#include <iostream>
#include <algorithm>
#include <map>
using namespace std;
int main()
{
	map <char, char> mirr{ {'b', 'd'}, {'d', 'b'}, {'p', 'q'}, {'q', 'p'}, {'i', 'i'}, {'o', 'o'}, {'v', 'v'}, {'w', 'w'}, {'x', 'x'} };
	string s;
	while (cin >> s && s != "#") {
		bool flag = true;
		for (char &c : s) {
			if (mirr.find(c) == mirr.end()) {
				flag = false;
				break;
			}
			c = mirr[c];
		}
		if (flag) {
			reverse(s.begin(), s.end());
			cout << s << "\n";
		} else cout << "INVALID\n";
	}
	return 0;
}