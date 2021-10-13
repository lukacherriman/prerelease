def is_prime(num, list):
    for i in range(len(list)):
        if num % list[i] == 0:
            return False
    return True


list = [2]
for i in range(2, 20000):
    if is_prime(i, list) == True:
        list.append(i)

print(list)
