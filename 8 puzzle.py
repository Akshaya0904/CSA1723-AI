goal = [1,2,3,4,5,6,7,8,0]
def print_board(state):
    for i in range(0,9,3):
        print(state[i:i+3])
def is_solved(state):
    return state == goal
state = [1,2,3,4,5,6,0,7,8]
print("Initial:")
print_board(state)
if is_solved(state):
    print("Already solved!")
else:
    print("Not solved yet.")
