L=[15,5,21,7,-1,0,2,-7,25,120,75,7,0]
def Quick(L):
    if len(L)<=1:
        return L
    pivot=L[0]
    left=[val for val in L[1:] if val<pivot]
    right=[val for val in L[1:] if val>=pivot]
    return Quick(left)+[pivot]+Quick(right)
print(Quick(L))