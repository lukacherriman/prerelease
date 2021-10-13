import random
thisdict = {
    "vanilla": (1000, 10, 1),
    "strawberry": (200, 20, 6),
    "raspberry": (300, 30, 5)

}
choice = random.choice(["vanilla", "strawberry", "raspberry"])
list = thisdict[choice]
list[0] -= 1
thisdict[choice] = list

print(thisdict)