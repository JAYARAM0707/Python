#153= 1^3+5^3+3

#using Loops
'''
num=int(input('Enter the number : '))
n=num
P=len(str(num))
res=0
while num!=0:
    res+=(num%10)**P
    num//=10
print('ArmStrong Number' if res==n else 'Not ArmStrong Number')
'''


#using Functions
'''
def ArmStrong(num,P,res=0):
    while num!=0:
        res+=(num%10)**P
        num//=10
    return res
num=int(input('enter the number : '))
P=len(str(num))
print('ArmStrong Number' if ArmStrong(num,P)==num else 'Not ArmStrong Number')
'''


#using Recursion
'''
def ArmStrong(num,P):
    if num ==0 :
        return 0
    return (num%10)**P +ArmStrong(num//10,P)
num=int(input('Enter the number : '))
P=len(str(num))
print('ArmStrong Number' if ArmStrong(num,P)==num else 'Not ArmStrong Number')
'''

#Using Filter Function

def ArmStrong(num,res=0):
    n=num
    P=len(str(num))
    while num!=0:
        res+=(num%10)**P
        num//=10
    return res==n
print(list(filter(ArmStrong,range(1,200))))