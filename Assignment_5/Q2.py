# Enter number of students from user. For those many students accept marks of 5
# subject marks from user and calculate percentage. Display all percentage and
# average percentage of students.


def calculate_percentage(marks):
    total_marks = sum(marks)
    percentage = total_marks / 5
    return percentage

def get_marks():
    marks = []
    for i in range(1,6):
        mark = float(input(f"Enter marks for subject {i}: "))
        marks.append(mark)
    return marks


def display_percentages(percentages):
    print("\nPercentages of students:")

    for i in range(len(percentages)):
        print(f"Student {i + 1}: {percentages[i]:.2f}%")

    average = sum(percentages) / len(percentages)

    print(f"\nAverage percentage of students: {average:.2f}%")


n = int(input("Enter number of students: "))
percentages = []

for i in range(n):
    print(f"\nEnter marks for student {i + 1}:")
    marks = get_marks()
    percentage = calculate_percentage(marks)
    percentages.append(percentage)


display_percentages(percentages)