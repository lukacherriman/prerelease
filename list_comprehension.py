def identity(nums):
    list2 = [i for i in nums]
    return list2


def doubled(nums):
    list2 = [i*2 for i in nums]
    return list2



def squared(nums):
    list2 = [i**2 for i in nums]
    return list2



def evens(nums):
    list2 = [i for i in nums if (i % 2 == 0)]
    return list2



def odds(nums):
    list2 = [i for i in nums if (i % 2 == 1)]
    return list2



def positives(nums):
    list2 = [i for i in nums if (i > 0)]
    return list2



def selective_stringify_nums(nums):
    list2 = [i for i in nums if (i % 5 == 0)]
    return list2



def words_not_the(sentence):
    """list2 = [i for i in ]
    pass"""



def vowels(word):
    list2 = [ch for ch in word if (ch in 'aeiou')]
    return list2



def vowels_set(word):
    list2 = ([ch for ch in word if (ch in 'aeiou')])
    return list2



def disemvowel(sentence):
    sentence1 = ''
    sentence2 = [ch for ch in sentence if (ch not in 'aeiou')]
    for ch in sentence2:
        sentence1 += ch
    return sentence1



def wiggle_numbers(nums):
    list2 = [i*2 for i in nums if (i % 2 == 0)]
    return list2



def encrypt_lol(sentence):
    sentence2 = ''
    sentence1 = [chr(ord(ch)+1) for ch in sentence]
    for ch in sentence1:
        sentence2 += ch
    return sentence2



nums = 'hello'
print(encrypt_lol(nums))