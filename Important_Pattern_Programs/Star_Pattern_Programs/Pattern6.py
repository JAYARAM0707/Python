# *       * 
#   *   * 
#     * 
#   *   * 
# *       * 

num=int(input('Enter the number : '))
for row in range(num):
    for col in range(num):
        if row==col or row+col==num-1:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()