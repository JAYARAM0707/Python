#     * 
#   * * * 
# * * * * * 

num=int(input('Enter the number : '))
for row in range(1,num+1):
    for sp in range(num-row):
        print(' ',end=' ')
    for col in range(2*row-1):
        print('*',end=' ')
    print()