def decimal_to_binary(number):
    binary_list = []
    while number > 0:
        binary_list.append(number % 2)
        number = number//2
    new = ""
    for i in range(len(binary_list)):
        new += str(binary_list[-(i+1)])
    return new


decimal_number = int(input("Enter a decimal number to be converted to binary: "))
print(decimal_to_binary(decimal_number))
