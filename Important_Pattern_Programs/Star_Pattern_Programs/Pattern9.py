# * * * * * 
#  * * * * 
#   * * * 
#    * * 
#     * 

num=int(input('Enter the number : '))
for row in range(1,num+1):
    for col in range(1,num+1):
        if row<=col:
            print('*',end=' ')
        else:
            print('',end=' ')
    print()