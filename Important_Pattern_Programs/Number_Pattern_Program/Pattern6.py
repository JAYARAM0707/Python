# 1 2 3 4 5 
# 6 5 4 3 2 
# 1 2 3 4 5 
# 6 5 4 3 2 
# 1 2 3 4 5 

num=int(input('Enter the number : '))
val=1
for row in range(1,num+1):
    for col in range(1,num+1):
        print(val,end=' ')
        if row % 2 ==0:
            val-=1
        else:
            val+=1
    print()