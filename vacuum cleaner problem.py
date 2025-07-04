rooms = ['dirty','dirty']
pos = 0
while 'dirty' in rooms:
    if rooms[pos]=='dirty':
        rooms[pos]='clean'
        print(f"Cleaned room {pos}")
    pos = 1 - pos
print("All rooms cleaned:", rooms)
