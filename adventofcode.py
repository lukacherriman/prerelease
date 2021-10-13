import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()


def product_sum_2020(file):
    for i in range(len(file)):
        file[i] = int(file[i])

    for num1 in file:
        for num2 in file:
            if num1 + num2 == 2020:
                return num1 * num2


def product_sum3_2020(file):
    for i in range(len(file)):
        file[i] = int(file[i])

    for num1 in file:
        for num2 in file:
            for num3 in file:
                if num1 + num2 + num3 == 2020:
                    return num1 * num2 * num3


file_path = filedialog.askopenfilename()
with open(file_path, 'r') as reader:
    file = reader.readlines()
    reader.close()

print(product_sum3_2020(file))
