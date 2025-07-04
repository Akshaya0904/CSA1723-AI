from collections import deque
g = {0:[1,2],1:[3],2:[4],3:[],4:[]}
visited = []
q=deque([0])
while q:
  n=q.popleft()
  if n not in visited:
    visited.append(n)
    q.extend(g[n])
print("BFS:", visited)
