#the number which is divisable by 1 and itself

#using for  loops
'''num=int(input('ennter the number : '))
count=0
for val in range(1,num+1):
    if num % val ==0:
        count+=1
print(num,'is Prime Number' if count==2 else ' is Not Prime Number ')'''

#above process while take more iterations
'''num=int(input('Enter the number : '))
if num>1:
    for val in range(2,num//2+1):
        if num % val == 0:
            print(num, 'is Not Prime Number ')
            break
    else:
        print(num," is Prime Number")
else:
    print(num, " is Not Prime Number")
'''

#below will take less iteration compare above both
'''num=int(input('enter the number : '))
if num>1:
    for val in range(2,int(num**0.5)+1):
        if num % val == 0 :
            print(num,'is Not Prime Number ')
            break
    else :
        print(num, 'is Prime Number ')

else:
    print(num, ' is Not Prime Number ')
'''

#using While loop
'''num=int(input('enter the number : '))
count=0
val=1
while val<num+1:
    if num%val ==0:
        count+=1
    val+=1
print(num,'is Prime Numnber ' if count==2 else 'is Not Prime Number')'''

#using Functions
'''
def Prime(num):
    if num>1:
        for val in range(2,num//2+1):
            if num%val==0:
                return False
        return True
    return False
num=int(input('Enter the number : '))
print( num,'is Prime Number' if Prime(num) else 'Not Prime Number')
'''

#using Recursions
'''
def Prime(num,val=2):
    if val==num//2+1:
        return True
    if num<2:
        return False
    if num%val==0:
        return False
    return Prime(num,val+1)
num=int(input('Enter the number : '))
print(num, 'is Prime Number ' if Prime(num) else 'Not Prime Number')
'''

# using Filter Functions
'''
def Prime(num):
    if num>1:
        for val in range(2,num//2+1):
            if num%val==0:
                return False
        return True
    return False
print(list(filter(Prime,range(1,25))))
'''

#print prime numbers in range 100 - 200 without using filter function
for num in range(100,200):
    for val in range(2,num//2+1):
        if num%val==0:
            break
    else:
        print(num,end=' ')
