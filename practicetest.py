number = 0
while number < 1 or number > 10:
    print('Enter a positive whole number')
    number = int(input())
    if number > 10:
        print('Number too large')
    elif number < 1:
        print('Not a whole number')

c = 1
for i in range(number):
    print(c)
    c = c*(number-1-i)/(i+1)