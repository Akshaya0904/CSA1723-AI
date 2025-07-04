import numpy as np
cities = np.array([[0,0],[1,2],[4,0],[6,3]])
tour = [0]
unvisited = set(range(1,len(cities)))
while unvisited:
    last = tour[-1]
    next_city = min(unvisited,key=lambda c:np.linalg.norm(cities[last]-cities[c]))
    tour.append(next_city)
    unvisited.remove(next_city)
tour.append(0)
print("TSP tour:", tour)
