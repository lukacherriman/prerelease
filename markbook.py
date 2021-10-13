"""Mark-book Homework"""


"defining list for class names and a 2 dimensional list for the scores"
class_score = []
name_list = []


"function to display the scores of students in list and average"


def display_scores():
    for i in range(len(name_list)):
        print(F"{name_list[i]}: {class_score[i]} - average is: {sum(class_score[i])/len(class_score[i])}")


"function to add a student and score or a score"


def add():
    name = input("Enter a name: ")
    try:
        b = name_list.index(name)
    except ValueError:
        class_score.append(name)
        name_list.append(name)
        b = name_list.index(name)
        class_score[b] = []
    else:
        ""
    class_score[b].append(int(input("Enter a score: ")))
    print(f"Average for {name} is {sum(class_score[b]) / len(class_score[b])}")


"while loop runs until an input is given to recur, asks for task and runs function "
recur = ""
while recur == "":
    task = int(input("Enter 1 to add a score, enter 2 to display scores: "))
    if task == 1:
        add()
    if task == 2:
        display_scores()
    recur = input("Enter anything to end program: ")




