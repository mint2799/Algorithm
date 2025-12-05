from collections import deque

n, k = map(int, input().split())
belt = [0] + list(map(int, input().split()))
visit = [False] * (2*n + 1)
robot = deque()

start = 1
end = n
cnt = 0
res = 0

def moveBelt():
    global start, end
    start -= 1
    end -= 1
    if start < 1: start = 2*n
    if end < 1: end = 2*n

def moveRobot():
    global cnt
    for _ in range(len(robot)):
        cur = robot.popleft()
        visit[cur] = False

        if cur == end: continue

        nxt = cur + 1
        if nxt > 2*n:
            nxt = 1

        if belt[nxt] >= 1 and not visit[nxt]:
            belt[nxt] -= 1
            if belt[nxt] == 0: cnt += 1
            if nxt == end: continue

            visit[nxt] = True
            robot.append(nxt)

        else:
            visit[cur] = True
            robot.append(cur)

def makeRobot():
    global cnt
    if not visit[start] and belt[start] >= 1:
        visit[start] = True
        belt[start] -= 1
        robot.append(start)
        if belt[start] == 0:
            cnt += 1

while cnt < k:
    res += 1
    moveBelt()
    moveRobot()
    makeRobot()
print(res)