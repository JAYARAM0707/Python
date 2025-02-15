L=[16,9,5,12,52,76,190,111]
target=112
#using for loop
'''
for val in range(len(L)):
    if L[val]==target:
        print(val)
        break
else:
    print(-1)
'''

#using While loop
'''
ind=0
while ind<len(L):
    if L[ind]==target:
        print(ind)
        break
    ind+=1
else:
    print(-1)
'''

#using Functions
'''
def Linear(L,target):
    for ind in range(len(L)):
        if L[ind]==target:
            return ind
    return -1
print(Linear(L,target))
'''

#using Recursions
def Linear(L,target,ind=0):
    if ind==len(L):
        return -1 
    if L[ind]==target :
        return ind
    return Linear(L,target,ind+1)
print(Linear(L,target))