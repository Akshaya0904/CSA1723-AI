def ab(depth,alpha,beta,maxp):
    if depth==3: return 5
    if maxp:
        alpha=max(alpha,ab(depth+1,alpha,beta,False))
        return alpha
    else:
        beta=min(beta,ab(depth+1,alpha,beta,True))
        return beta
print("AlphaBeta result:", ab(0,-99,99,True))
