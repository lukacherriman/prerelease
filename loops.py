import random
score = 0
for i in range(10):
    x = random.randint(1, 10)
    y = random.randint(1, 10)
    answer = int(input(f" {x} + {y} = "))
    if answer == x+y:
        score += 1
        print("Correct")
    else:
        print("Incorrect")
print(f"Score is {score}")

