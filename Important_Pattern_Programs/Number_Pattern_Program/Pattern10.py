#         1 
#       1 3 1
#     1 4 7 4 1
#   1 5 9 13 9 5 1
# 1 6 11 16 21 16 11 6 1

num=int(input("Enter the number : "))
for row in range(1,num+1):
    val=1
    for sp in range(num-row):
        print(' ',end=' ')
    for col in range(1,2*row):
        print(val,end=' ')
        if col<row:
            val+=row
        else:
            val-=row
    print()