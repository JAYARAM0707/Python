# * 
#   * 
#     * 
#       * 
#         * 

num=int(input('enter the number : '))
for row in range(num+1):
    for col in range(num+1):
        if row==col:
            print('*',end=' ')
        else :
            print(' ',end=' ')
    print()