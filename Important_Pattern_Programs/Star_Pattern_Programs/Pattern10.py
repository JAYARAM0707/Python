#         * 
#       * * * 
#     * * * * * 
#   * * * * * * * 
# * * * * * * * * * 
#   * * * * * * * 
#     * * * * * 
#       * * * 
#         * 

num=int(input('Enter the number : '))
star=1
space=num//2
for row in range(num):
    for sp in range(space):
        print(' ',end=' ')
    for st in range(star):
        print('*',end=' ')
    if row<num//2:
        star+=2
        space-=1
    else :
        star-=2
        space+=1
    print()