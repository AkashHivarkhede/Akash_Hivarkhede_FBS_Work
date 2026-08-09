# Python Program to Find the Intersection of Two Lists

def find_intersection(li1 , li2):
    intersection = []

    for i in li1:
        for j in li2:
            if i == j:
                intersection.append(i)
                break

    print("Intersection of the two lists:", intersection)
    


li1 = [10 , 20 , 30 , 40]
li2 = [30 , 40 , 50 , 60]

find_intersection(li1, li2)
