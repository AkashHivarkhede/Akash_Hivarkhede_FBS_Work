# Print 1 to 100 in snakes and ladder pattern.


def ladder_pattern():

    start = 1
    rows = [] 

    for i in range(10):
        row = []
        for j in range(10):
            row.append(start)
            start += 1
        
        rows.append(row)  # adding number 1 to 100


    for i in range(9 , -1 , -1):
        
        if i % 2 == 0:
            for num in rows[i]:
                print(f'{num:3}', end = " ")
        else:
            for j in range(9 , -1 , -1):
                print(f"{rows[i][j]:3}" , end=" ")
        
        print()

ladder_pattern()