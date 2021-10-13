def hashfunc(key):
    sum = 0
    for i in range(len(key)):
        sum += ord(key[i])**2
    hash = sum % 523
    return hash

list = []
for i in range(523):
    list.append([])

words_list = ['PEN','PLUME','CAT','CHAT','NOW','MAINTENANT','WON','GAGNE']
for i in range(0,len(words_list),2):
    loop = True
    displace = 0

    while loop == True:
        if list[hashfunc(words_list[i])+displace] == []:
            list[hashfunc(words_list[i])+displace].append(words_list[i])
            list[hashfunc(words_list[i])+displace].append(words_list[i+1])
            loop = False
        else:
            displace += 1



print(list)
data = input('Enter word to search for')
french = bool(input('Enter True for the french word'))

value = hashfunc(data)

if french == True:
    print(list[value][1])
else:
    print(list[value][1])
