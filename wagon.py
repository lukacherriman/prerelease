class Wagon:
    def __init__(self, owner_name, weight, no_wheels):
        self.owner_name = owner_name
        self.weight = weight
        self.number_of_wheels = no_wheels

    def get_owner_name(self):
        return self.owner_name

    def get_weight(self):
        return self.weight

    def get_number_of_wheels(self):
        return self.number_of_wheels


class ClosedWagon(Wagon):
    def __init__(self, height, no_doors, suitable_food, owner_name, weight, no_wheels):
        super().__init__(owner_name, weight, no_wheels)
        self._height = height
        self._number_of_doors = no_doors
        self._suitable_for_food = suitable_food

    def get_height(self):
        return self._height

    def get_number_of_doors(self):
        return self._number_of_doors

    def get_suitable_for_food(self):
        return self._suitable_for_food


class OpenWagon(Wagon):
    def __init__(self, owner_name, weight, no_wheels):
        super().__init__(owner_name, weight, no_wheels)


class Yard:
    def __init__(self, wagons):
        self._wagons = wagons

    def wagon_enter(self, other):
        self._wagons.append(other)
        return


class Siding:
    def __init__(self, size, wagons):
        self._size = size
        self._wagons = wagons

    def pop_cart(self):
        cart = self._wagons.pop()
        return cart

    def push_cart(self, other):
        self._wagons.append(other)
        return
