def hexadecimal_conversion(number):
    hex_list = []
    values_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'A', 'B', 'C', 'D', 'E', 'F']
    while number > 0:
        hex_list.append(number % 16)
        number = number//16
    hex_list.reverse()
    hex_string = ""
    for i in hex_list:
        hex_string += str(values_list[i])
    return hex_string


def binary_conversion(number):
    binary_list = []
    while number > 0:
        binary_list.append(number % 2)
        number = number // 2
    binary_list.reverse()
    bin_string = ""
    for i in binary_list:
        bin_string += str(i)
    return bin_string


print(hexadecimal_conversion(123))
print(binary_conversion(123))