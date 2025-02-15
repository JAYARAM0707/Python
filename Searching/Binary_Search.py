L=[2,3,5,7,12,15,18,19,25,50]
target=51
li=0
hi=len(L)-1

# using loops

'''
while li<=hi:
    ind=(hi+li)//2
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
def Binary(L,target,li,hi):
    while li<=hi:
        ind=(hi+li)//2
        if L[ind]==target:
            return ind
        elif L[ind]<target:
            li =ind+1
        elif L[ind]>target:
            hi=ind-1
    return -1
print(Binary(L,target,li,hi))
'''

#using Recursion
def Binary(L,target,li,hi):
    if li>hi:
        return -1
    ind=(hi+li)//2
    if L[ind]==target:
        return ind
    elif L[ind]<target:
        return Binary(L,target,ind+1,hi)
    elif L[ind]>target:
        return Binary(L,target,li,ind-1)
print(Binary(L,target,li,hi))