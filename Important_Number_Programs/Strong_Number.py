#145=1!+4!+5!

#using loops
'''
num=int(input('enter the number : '))
n=num
res=0
while num!=0:
    a=num%10
    fact=1
    for val in range(1,a+1):
        fact*=val
    res+=fact
    num//=10
print('Strong Number' if res==n else 'Not Strong Number')
'''

#using functions
'''
def Strong(num,res=0):
    while num!=0:
        res+=Factorial(num%10)
        num//=10
    return res

def Factorial(num,fact=1):
    for val in range(1,num+1):
        fact*=val
    return fact
num=int(input('enter the number : '))
print('Strong Number' if Strong(num)==num else 'Not Strong Number')
'''


#using recursion 

def Strong(num):
    if num==0:
        return 0
    return Factorial(num%10) + Strong(num//10)

def Factorial(num):
    if num==0 or num==1:
        return 1
    return num*Factorial(num-1)
num=int(input('enter the number : '))
print('Strong Number ' if Strong(num)==num else 'Not Strong Number')


#using filter function

def Strong(num,res=0):
    n=num
    while num!=0:
        res+=Factorial(num%10)
        num//=10
    return res==n

def Factorial(num,fact=1):
    for val in range(1,num+1):
        fact*=val
    return fact
print(list(filter(Strong,range(1,150))))
