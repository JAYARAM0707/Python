# 1 2 3 4 5 
# 1 2 3 4 5 
# 1 2 3 4 5 
# 1 2 3 4 5 
# 1 2 3 4 5 

num=int(input('Enter the number : '))
for row in range(1,num+1):
    for col in range(1,num+1):
        print(col,end=' ')
    print()