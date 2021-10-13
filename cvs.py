class Engine:
    def __init__(self, name, weight, colour):
        self.name = name
        self.weight = weight
        self.colour = colour

    def display_engine(self):
        print(f"Engine name: {self.name}, weight: {self.weight}, colour: {self.colour}")



engines_list = []
engines_list.append(Engine('Thomas', 600, 'blue'))
engines_list.append(Engine('James', 650, 'red'))
engines_list.append(Engine('Edward', 1000, 'blue'))
engines_list.append(Engine('Gordon', 2500, 'blue'))
engines_list.append(Engine('Henry', 2100, 'green'))


def display_engines(engines):
    for e in engines_list:
        e.display_engine()


def write_file(engines):
    csv_list = ['Engine name,Engine Weight,Engine Colour\n']
    for i in range(len(engines_list)):
        next_column = f"{engines_list[i].name}, {str(engines_list[i].weight)}, {engines_list[i].colour}\n"
        csv_list.append(next_column)

    with open('engines.csv', 'w') as writer:
        for j in range(len(csv_list)):
            writer.write(csv_list[j])


def read_file():
    with open('engines.csv', 'r') as reader:
        data = reader.readlines()[1:]
        new = ''
        for i in range(len(data)):
            new_list = []
            for ch in data[i]:
                if ch == ',' or ch == '\n':
                    new_list.append(new)
                    new = ''
                else:
                    new += ch
            print(f"{new_list[0]}, {new_list[1]}, {new_list[2]}")


def add_engine(engine):
    name = input("Enter name of engine: ")
    weight = int(input("Enter weight of engine: "))
    colour = input("Enter colour of engine: ")
    engines_list.append(Engine(name, weight, colour))


add_engine(engines_list)
write_file(engines_list)
read_file()
