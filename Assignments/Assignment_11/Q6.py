# Python Program to Find the Union of two Lists

def find_union(li1 , li2):
     union = [] 
     for i in li1:
          union.append(i)
     for i in li2:
          found = False
          
          for j in union:
               if j == i:
                    found = True
                    break
          if found == False:
               union.append(i)
     
     print("Union of the two lists: " , union)
    


li1 = [10 , 20 , 30 , 40]
li2 = [30 , 40 , 50 , 60]

find_union(li1, li2)
