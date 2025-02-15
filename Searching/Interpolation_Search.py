L=[2,3,5,7,12,15,18,19,25,50]
target=51
li=0
hi=len(L)-1
#using loops
'''
while li<=hi and L[li]<=target<=L[hi]:
    ind=int(li+((hi-li)/(L[hi]-L[li]))*(target - L[li]))
    if L[ind]==target:
        print(ind)
        break
    elif L[ind]<target:
        li=ind+1
    elif L[ind]>target:
        hi=ind-1
else:
    print(-1)
'''

#using Functions
'''
def Interpolation(L,target,li,hi):
    while li<=hi and L[li]<=target<=L[hi]:
        ind=int(li+((hi-li)/(L[hi]-L[li]))*(target - L[li]))
        if L[ind]==target:
            return ind
        elif L[ind]<target:
            li=ind+1
        elif L[ind]>target:
            hi=ind-1
    return -1
print(Interpolation(L,target,li,hi))
'''

#using Recursions
def Interpolation(L,target,li,hi):
    if li>hi or L[li]>target or L[hi]<target:
        return -1
    ind=int(li+((hi-li)/(L[hi]-L[li]))*(target - L[li]))
    if L[ind]==target:
        return ind
    elif L[ind]<target:
        return Interpolation(L,target,ind+1,hi)
    elif L[ind]>target:
        return Interpolation(L,target,li,ind-1)
print(Interpolation(L,target,li,hi))
    