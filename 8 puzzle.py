from queue import Queue
def bfs(start,goal):
    q=Queue()
    q.put(start)
    visited=set()
    while not q.empty():
        state=q.get()
        print(state)
        if state==goal:
            print("Goal reached")
            return
        visited.add(tuple(state))
bfs([1,2,3,4,5,6,7,8,0],[1,2,3,4,5,6,7,8,0])
