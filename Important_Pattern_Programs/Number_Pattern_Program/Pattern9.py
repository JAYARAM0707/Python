#      5
#   4  3  2
# 1 0 -1 -2 -3

val=5
num=int(input('enter the number : '))
for row in range(1,num+1):
    for sp in range(num-row):
        print(' ',end=' ')
    for col in range(2*row-1):
        print(val,end=' ')
        val-=1
    print()
        