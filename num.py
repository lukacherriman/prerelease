import math

def palendrome(num):
    count = 0
    while True:
        num = num + reverse(num)
        print(num)
        count += 1
        if check_palendrome(num) or count == 1000:
            return num, count

def reverse(num):
    string_num = str(num)[::-1]
    num = int(string_num)
    return num

def check_palendrome(num):
    string_num = str(num)
    first_half = string_num[0:math.ceil(len(string_num)/2)]
    second_half = string_num[math.floor(len(string_num)/2):]
    second_half = str(reverse(second_half))
    print(first_half, second_half)

    if first_half == second_half:
        return True



num = int(input("Enter number: "))
print(palendrome(num))
