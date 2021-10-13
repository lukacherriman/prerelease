def cat_dog_same(test_string):
    cats = test_string.count('cat')
    dogs = test_string.count('dog')
    return cats == dogs


def double_characters(test_string):
    new = ""
    for ch in test_string:
        new += 2*ch
    return new


def rotate_string(test_string, n):
    string = test_string
    for i in range(n):
        new = ''
        for ch in range(len(string)):
            new += string[ch-1]
        string = new
    return string


def letters_in_words(test_string):
    letters_list = []
    new = ''
    for ch in test_string:
        if ch == ' ':
            letters_list.append(len(new))
            new = ''
        else:
            new += ch
    if test_string[len(test_string)-1] != ' ':
        letters_list.append(len(new))
    return letters_list


def add_spaces(test_string, list):
    new = ''
    k = 0
    for i in range(len(list)):
        for j in range(list[i]):
            new += test_string[k]
            k += 1
        new += ' '
    return new





print(rotate_string('this is a few words',10))
print(add_spaces('thisisafewwords',[4,2,1,3,5]))

'''
Well done. I think you could have done letters_in_words() more easily by using the string.split() function. Make
sure you know how that works.
'''
