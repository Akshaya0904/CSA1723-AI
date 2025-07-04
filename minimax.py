def minimax(depth,maxp):
    return 10-depth if maxp else depth-10
print("Best score:", minimax(2,True))
