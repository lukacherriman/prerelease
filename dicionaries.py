capitals = {
    "England": "London",
    "France": "Paris",
    "Germany": "Berlin"
}


def print_dict():
    print(capitals)


def print_object():
    key = input("Enter country name: ")
    print(capitals[key])


def delete():
    key = input("Enter country name: ")
    del capitals[key]
    print(capitals)


def add():
    key = input("Enter country name: ")
    city = input("Enter countries capital: ")
    capitals[key] = city
    print(capitals)


def main():
    task = int(input("""
    For task enter:
    1. Print entire dictionary
    2. Print single item from dictionary 
    3. Remove an item from the dictionary
    4. Add an item to the dictionary
    : """))
    if task == 1:
        print_dict()
    elif task == 2:
        print_object()
    elif task == 3:
        delete()
    elif task == 4:
        add()

main()