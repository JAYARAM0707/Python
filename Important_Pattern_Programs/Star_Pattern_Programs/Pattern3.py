# * * * * *  
# * * * *  
# * * *  
# * *  
# * 

num=int(input('Enter the number : '))
for row in range(num,0,-1):
    for col in range(row):
        print('*',end=' ')
    print()
