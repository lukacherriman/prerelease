task_list =[]


def add():
    task_list.append(input("What task would you like to add? : "))


def display_task():
    for i in range(len(task_list)):
        print(task_list[i])


def check_next():
    try:
        print(task_list[0])
    except:
        ValueError


def complete_next():
    print(f"This task has been removed: {task_list[0]}")
    task_list.pop(0)


def main():
    loop = True
    while loop == True:
        job = int(input("""What would you like to do?
        1. Add a task
        2. Display all tasks
        3. Check the next task
        4. Complete the next task
        5. Quit
        : """))
        if job == 1:
            add()
        elif job == 2:
            display_task()
            input("//ENTER//")
        elif job == 3:
            check_next()
            input("//ENTER//")
        elif job == 4:
            complete_next()
            input("//ENTER//")
        else:
            loop = False

main()

"""
Well done for including a try except block. Your syntax isn't quite correct. It should look like
try:
    print(task_list[0])
except ValueError:
    pass
    # Or do something like display a message.
    
This would catch the Value error but any other errors would cause the program to halt. If you have except: on it's own
it will catch any errors at all (which isn't usually what you want).
"""
