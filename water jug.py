from collections import deque
q=deque([(0,0)])
visited=set()
while q:
    a,b=q.popleft()
    if a==2 or b==2:
        print("Solution found:",a,b)
        break
    visited.add((a,b))
    # actions
    q.extend([(4,b),(a,3),(0,b),(a,0),
              (min(a+b,4), max(0,b-(4-a))),
              (max(0,a-(3-b)), min(a+b,3))])
