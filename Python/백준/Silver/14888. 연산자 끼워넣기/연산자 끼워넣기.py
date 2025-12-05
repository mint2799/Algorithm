N = int(input())
a = list(map(int,input().split()))
operator = list(map(int,input().split()))
mx = -1e9
mn = 1e9

def dfs(n, res):
    global mx,mn
    
    if n == N-1:
        mx = max(res, mx)
        mn = min(res, mn)
        return
    
    if operator[0] != 0:
        operator[0] -= 1
        dfs(n+1, res+a[n+1])
        operator[0] += 1
            
    if operator[1] != 0:
        operator[1] -= 1
        dfs(n+1, res-a[n+1])
        operator[1] += 1
            
    if operator[2] != 0:
        operator[2] -= 1
        dfs(n+1, res*a[n+1])
        operator[2] += 1
            
    if operator[3] != 0:
        operator[3] -= 1
        dfs(n+1, int(res/a[n+1]))
        operator[3] += 1
dfs(0, a[0])
print(mx,mn)