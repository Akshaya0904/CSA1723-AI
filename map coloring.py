colors = ['R','G','B']
neighbors = {'A':['B','C'],'B':['A','C'],'C':['A','B']}
assign = {}
def backtrack(varlist):
    if not varlist:
        return assign
    var=varlist[0]
    for c in colors:
        if all(assign.get(n)!=c for n in neighbors.get(var,[])):
            assign[var]=c
            if backtrack(varlist[1:]):
                return assign
            assign.pop(var)
    return False
result = backtrack(['A','B','C'])
print("Map coloring:", result)
