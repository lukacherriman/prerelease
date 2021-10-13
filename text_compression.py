def compress_string(string):
    new = ""
    count = 0
    new += string[0]
    for ch in string:
        if new[-1] == ch:
            count += 1
        else:
            new += " "
            new += str(count)
            count = 1
            new += " "
            new += ch
    new += ' '
    new += str(count)
    return new


def decompress_string(string):
    new = ''
    for i in range(0, len(string), 4):
        character = string[i]
        repeat = string[i+2]
        new += int(repeat)*character
    return new


string = input("Enter the text you would like to compress: ")
compressed = (compress_string(string))
print(compressed)
print(decompress_string(compressed))
