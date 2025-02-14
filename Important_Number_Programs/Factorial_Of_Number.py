#5!=5*4*3*2*1=120

#using for loop 
'''num=int(input('enter the number : '))
fact=1
for val in range(1,num+1):
    fact*=val
print(fact)

#or

for val in range(num,0,-1):
    fact*=val
print(fact)
'''


#using while loop

'''
num=int(input('enter the number : '))
fact=1
ind=1
while ind<num+1:
    fact*=ind
    ind+=1
print(fact)

# or

while num>0:
    fact*=num
    num-=1 
print(fact)
'''

#using functions
'''def Factorial(num,fact=1):
    for val in range(1,num+1):
        fact*=val
    return fact
num=int(input('enter the number : '))
print(Factorial(num))'''

#using Recursions
'''def Factorial(num,val=1):
    if val==num+1:
        return 1
    return val*Factorial(num,val+1)
num=int(input('Enter the number : '))
print(Factorial(num))'''

# or

def Factorial(num):
    if num==0 or num==1:
        return 1
    return num*Factorial(num-1)
num=int(input('Enter the number : '))
print(Factorial(num))
