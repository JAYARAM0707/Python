# 1 2 3 4 5 
# 2 3 4 5 6 
# 3 4 5 6 7 
# 4 5 6 7 8 
# 5 6 7 8 9 

num=int(input('Enter the number : '))
for row in range(1,num+1):
    val=row
    for col in range(1,num+1):
        print(val,end=' ')
        val+=1
    print()