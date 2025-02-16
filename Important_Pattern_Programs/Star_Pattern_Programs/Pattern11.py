# *
# * *
# *   *
# *     *
# * * * * *

num=int(input('Enter the number : '))
for row in range(num):
    for col in range(num):
        if col==0 or row==num-1 or row==col:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()