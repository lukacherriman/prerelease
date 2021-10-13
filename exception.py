usernames = ['Cheetara', 'Lion-O', 'Snarf', 'Tygra', 'Panthro', 'Mumm-Ra']

def login_unhandled(usernumber):
    print("\n -- The Basic Verson \n")
    try:
        number = int(usernumber)
        print(f"Welcome {usernames[number]}, user number {number}")
    except ValueError:
        print("value error cannot turn a string into integer")
    try:
        division = 301 / number
        print(f"301 divided by {number} = {division}")
    except ZeroDivisionError:
        print("Error divided by zero")

while True:
    inp = input("\nType in a number: ")
    login_unhandled(inp)