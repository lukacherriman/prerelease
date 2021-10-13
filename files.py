import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()


def read_file(file):
    with open(file, 'r') as reader:
        file = reader.readlines()

    print(file)


def write_file(file):
    with open(file, 'w') as writer:
        line = input('Enter line in text file enter // to end: ')
        if line != '//':
            writer.write(line)
            writer.write('\n')
        while line != "//":
            line = input('Enter next line in text file enter // to end: ')
            if line != '//':
                writer.write(line)
                writer.write('\n')


def file_path():
    file = filedialog.askopenfilename()
    return file


def main():
    selection = ""
    # file = 'C:/PythonFiles/files.txt'
    file = 'files.txt'
    while selection != "END":
        print("""   
        To read the file type r:
        To write to the file type w:
        To select a file type s:
        To end the program type END: """)
        selection = input()
        if selection == "r":
            read_file(file)
        elif selection == "w":
            write_file(file)
        elif selection == "s":
            file = file_path()


main()

"""
Luka. Ok, this mostly works but there are a few improvements that could be made.
On line 12 you are printing a list of strings which doesn't format very nicely. It's better to
iterate through the list and print each line separately. 
"""
