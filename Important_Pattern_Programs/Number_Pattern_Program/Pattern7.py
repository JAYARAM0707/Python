#         1  
#       2 2  
#     3 3 3 
#   4 4 4 4 
# 5 5 5 5 5 

num=int(input('Enter the number : '))
for row in range(1,num+1):
    for sp in range(num-row):
        print(' ',end=' ')
    for col in range(row):
        print(row,end=' ')
    print()