#include<iostream>
#include<vector>
#include<queue>
using namespace std;
int n, k, Start, End, res = 0, cnt = 0;
vector<int> belt;
vector<bool> visit;
queue<int> robot;
void MoveBelt();
void MoveRobot();
void AddRobot();

int main() {
	cin >> n >> k;
	Start = 1;
	End = n;
	belt.resize(2 * n + 1);
	visit.assign(2 * n + 1, false);

	for (int i = 1; i <= 2 * n; i++) cin >> belt[i];
	while (cnt < k){
		res++;
		MoveBelt();
		MoveRobot();
		AddRobot();
	}
	cout << res << "\n";
	return 0;
}
void MoveBelt() {
	Start--;
	End--;
	if (Start < 1) Start = 2 * n;
	if (End < 1) End = 2 * n;
}
void MoveRobot() {
	int Size = robot.size();
	for (int i = 0; i < Size; i++) {
		int cur = robot.front();
		visit[cur] = false;
		robot.pop();

		if (cur == End) continue;

		int next = cur + 1;
		if (next > 2 * n) next = 1;
		if (belt[next] > 0 && visit[next] == false) {
			belt[next]--;
			if (belt[next] == 0) cnt++;
			if (next == End) continue;
			visit[next] = true;
			robot.push(next);
		}
		else {
			visit[cur] = true;
			robot.push(cur);
		}
	}
}
void AddRobot() {
	if (visit[Start] == false && belt[Start] > 0) {
		visit[Start] = true;
		belt[Start]--;
		robot.push(Start);
		if (belt[Start] == 0) cnt++;
	}
}