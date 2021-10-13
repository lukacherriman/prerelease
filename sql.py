import sqlite3
import datetime

def main(connection):
    while True:
        print("""
-----MENU OPTIONS-----
1. View List
2. Add item to list
3. Mark as done 
4. Sort by due date 
5. Filter by category 
                 """)

        choice = int(input())
        if choice == 1:
            view(connection)
        elif choice == 2:
            add(connection)
        elif choice == 3:
            mark(connection)
        elif choice == 4:
            sort_date(connection)
        elif choice == 5:
            filter_cat(connection)
        else:
            break

def view(connection):
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM ToDoList")
    while True:
        result = cursor.fetchone()
        if result is None:
            break
        print(result)

    connection.commit()

def add(connection):
    description = input("Enter description of task: ")
    category = input("Enter category: ")
    due_date = input("Enter due date  (dd-mm-yyyy): ")
    date_created = datetime.datetime.today().strftime('%d-%m-%Y')
    cursor = connection.cursor()
    cursor.execute(f""" 
                    INSERT INTO ToDoList (Description, Completed, Category, DueDate, DateCreated)
                    VALUES('{description}', False, '{category}', {due_date}, {date_created})
    
    """)

def mark(connection):
    id_selected = int(input('Enter the Id of the completed task: '))
    date_completed = datetime.datetime.today().strftime('%d-%m-%Y')
    cursor = connection.cursor()
    cursor.execute(f""" 
                    UPDATE ToDoList
                    SET Completed = True,
                    DateCompleted = {date_completed}
                    WHERE ItemId = {id_selected}
                    
    """)

def sort_date():
    return

def filter_cat(connection):
    cursor = connection.cursor()
    category = input('Enter category to filter by: ')
    cursor.execute(f"""
                    SELECT * FROM ToDoList
                    WHERE Category = {category}
    """)
    while True:
        result = cursor.fetchone()
        if result is None:
            break
        print(result)


connection = sqlite3.connect('chinook.db')

main(connection)
connection.close
