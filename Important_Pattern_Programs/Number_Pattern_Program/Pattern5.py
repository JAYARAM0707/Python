# 1 2 3 4 5 
# 2 4 6 8 10 
# 3 4 5 6 7  
# 4 6 8 10 12  
# 5 6 7 8 9  

num=int(input('Enter the number : '))
for row in range(1,num+1):
    val=row
    for col in range(1,num+1):
        print(val,end=' ')
        if row%2==0:
            val+=2
        else:
            val+=1
    print()