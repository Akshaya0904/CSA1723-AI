from heapq import heappush,heappop
start,goal=(0,0),(2,2)
def h(a,b): return abs(a[0]-b[0])+abs(a[1]-b[1])
open=[(0,start)]
came={}
while open:
    _,curr=heappop(open)
    if curr==goal:
        break
    for dx,dy in [(0,1),(1,0),(0,-1),(-1,0)]:
        next=(curr[0]+dx,curr[1]+dy)
        if 0<=next[0]<=2 and 0<=next[1]<=2:
            came[next]=curr
            heappush(open,(h(next,goal),next))
print("Path found to",goal)
