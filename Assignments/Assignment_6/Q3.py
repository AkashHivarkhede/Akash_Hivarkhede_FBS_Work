
#      1
#     1  1
#    1  2  1
#   1  3  3  1


for i in range(0 , 4):
    for j in range(0 , 4 - i):
        print('_' , end = ' ')
    for j in range(0 , i + 1):
        print('1' , end = ' ')
    for j in range(0 , i):
        print('1' , end = ' ')
    print()