def divide(L):
    if len(L)<=1:
        return L
    left=L[:len(L)//2]
    right=L[len(L)//2:]
    divide(left),divide(right)
    Merge(L,left,right)

def Merge(L,left,right):
    mi,li,ri=0,0,0
    while li<len(left) and ri<len(right):
        if left[li]<right[ri]:
            L[mi]=left[li]
            li+=1
        else:
            L[mi]=right[ri]
            ri+=1
        mi+=1
    while li<len(left):
        L[mi]=left[li]
        li+=1
        mi+=1
    while ri<len(right):
        L[mi]=right[ri]
        ri+=1
        mi+=1

L=[15,5,21,7,-1,0,2,-7,25,120,75,7,0]
divide(L)
print(L)