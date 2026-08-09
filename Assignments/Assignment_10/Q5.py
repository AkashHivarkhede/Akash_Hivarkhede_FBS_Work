# Accept a number from user and check if this element is present in the list or
# not. Also tell how many times it is present in the list.

def linear_search(list,search):
    count = 0
    for i in range(0 , len(list)):
        if list[i] == search:
            count += 1
        
    if count == 0:
        return -1
    else:
        return count
            
list = [10 , 20 , 30 , 40 , 50 , 40 , 30 , 20 , 10 , 20 , 10 ]
search = int(input('Enter a element you want to search :'))
res = linear_search(list, search)
if res != -1:
    print(search,'is present in the list.' , res ,'times.')
else:
    print(search ,'is not present in the list.')