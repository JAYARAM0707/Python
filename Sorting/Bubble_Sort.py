L=[15,5,21,7,-1,0,2,-7,25,120,75]
for ind in range(len(L)-1,0,-1):
    for ind1 in range(ind):
        if L[ind]<L[ind1]:
            L[ind],L[ind1]=L[ind1],L[ind]
            
print(L)