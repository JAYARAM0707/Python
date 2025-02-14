# *  
# * *  
# * * *  
# * * * *  
# * * * * *

num=int(input('Enter the number : '))
for row in range(0,num+1):
    for col in range(row):
        print('*',end=' ')
    print()