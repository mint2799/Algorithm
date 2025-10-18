#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
int main()
{
	int n;
	cin >> n;
	vector <string> names;
	for (int i = 0; i < n; i++)
	{
		string name;
		cin >> name;
		if (name.size() == 3)
			names.push_back(name);
	}
	sort(names.begin(),names.end());
	cout << names[0] << "\n";
	return 0;
}