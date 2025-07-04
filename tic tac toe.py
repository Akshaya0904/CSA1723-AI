b = [' ']*9
def show():
    for i in range(0,9,3): print(b[i:i+3])
b[0]=b[4]=b[8]='X'
show()
if b[0]==b[4]==b[8]!=' ':
    print("X wins")
