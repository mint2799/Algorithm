def dfs(graph, start):
  visited = set()
  stack = [start]
  while stack:
    node = stack.pop()
    if node not in visited:
      visited.add(node)
      for neighbor in reversed(graph[node]):
        if neighbor not in visited:
          stack.append(neighbor)
  return len(visited)-1

n = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(int(input())):
  u,v = map(int,input().split())
  graph[u].append(v)
  graph[v].append(u)
print(dfs(graph, 1))