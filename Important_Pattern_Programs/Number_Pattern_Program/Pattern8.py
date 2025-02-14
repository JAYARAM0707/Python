#         1 
#       2 2 2 
#     3 3 3 3 3 
#   4 4 4 4 4 4 4 
# 5 5 5 5 5 5 5 5 5 
#   6 6 6 6 6 6 6 
#     7 7 7 7 7 
#       8 8 8 
#         9 

num=int(input('Enter the number :  '))
val=1
space=num//2
for row in range(1,num+1):
    for sp in range(space):
        print(' ',end=' ')
    for col in range(val):
        print(row ,end=' ')
    if row<num//2+1:
        space-=1
        val+=2
    else:
        space+=1
        val-=2
    print()