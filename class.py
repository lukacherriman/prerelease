class Animal:
    def __init__(self, state, size, diet, fed):
        self._state = state
        self._size = size
        self._diet = diet
        self._fed = fed


dog = Animal("dog", 1, 10, False)


def feed(size, diet, fed, food):
    if fed == True:
        return size, fed
    else:
        if food >= diet:
            fed = True
            size += 1
            return size, fed
        else:
            return size, fed

size = feed(dog._size, dog._diet, dog._fed, 10)[0]
fed = feed(dog._size, dog._diet, dog._fed, 10)[1]
print(f"dog fed is {fed} the current size of dog is {size}")