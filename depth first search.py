g = {0:[1,2],1:[3],2:[4],3:[],4:[]}
visited = []
def dfs(n):
  if n not in visited:
    visited.append(n)
    for i in g[n]: dfs(i)
dfs(0)
print("DFS:", visited)
