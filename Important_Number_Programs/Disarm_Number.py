#135 = 1^1 + 3^2 + 5^3

#using for loop
'''
num=int(input('Enter the number : '))
n=num
P=len(str(num))
res=0
while num!=0:
    res+=(num%10)**P
    P-=1
    num//=10
print('DisArm Number' if res==n else 'Not DisArm Number')
'''

#using Functions 
'''
def DisArm(num,P,res=0):
    while num!=0:
        res+=(num%10)**P
        P-=1
        num//=10
    return res
num=int(input('enter the number  : '))
P=len(str(num))
print('DisArm Number' if DisArm(num,P) else 'Not DisArm Number')
'''

#using Recursion
'''
def DisArm(num,P):
    if num ==0 :
        return 0
    return (num%10)**P + DisArm(num//10,P-1)
num=int(input('enter the number : '))
P=len(str(num))
print('Disarm Number' if DisArm(num,P)==num else 'Not Disarm Number')
'''

#using Filter function
def DisArm(num,res=0):
    n=num
    P=len(str(num))
    while num!=0:
        res+=(num%10)**P
        P-=1
        num//=10
    return res==n
print(list(filter(DisArm,range(1,200))))
