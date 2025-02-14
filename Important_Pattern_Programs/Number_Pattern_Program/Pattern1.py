# 1 1 1 1 1  
# 2 2 2 2 2  
# 3 3 3 3 3  
# 4 4 4 4 4  
# 5 5 5 5 5

num=int(input('Enter the number : '))
for row in range(1,num+1):
    for col in range(1,num+1):
        print(row,end=' ')
    print()