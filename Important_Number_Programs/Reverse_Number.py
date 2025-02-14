#using loops
#1st way
'''
num=int(input('Enter the number : '))
n=num
rev=0
while num!=0:
    rev=(num%10)+rev*10
    num//=10 
print(rev)
'''
#2nd way
'''
num=int(input('Enter the number : '))
rev=0
C=len(str(num))-1
while num!=0:
    rev+=(num%10)*10**C
    C-=1
    num//=10
print(rev)
'''

#using Function
'''
def Reverse(num,rev=0):
    while num!=0:
        rev=(num%10)+rev*10
        num//=10
    return rev
num=int(input('Enter the number : '))
print(Reverse(num))
'''

#using Recursion
def Reverse(num,c):
    if num==0:
        return 0
    return (num%10)*10**c +Reverse(num//10,c-1)
num=int(input('Enter the number : '))
c=len(str(num))-1
print(Reverse(num,c))
