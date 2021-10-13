name_list = ["ed", "will", "toby", "ched", "lisa", "greg", "john", "paul", "marry"]

for i in range(3):
    name = input("Type in a name ")
    name_list.append(name)

print(name_list)
print(name_list[2])
print(name_list[-7:])

num_list = []
for i in range(5):
    num_list.append(int(input("type a number ")))
print("largest number is " + str(max(num_list)))
print("smallest number is " + str(min(num_list)))
print("total of list is " + str(sum(num_list)))
print("average of list is " + str(sum(num_list)/len(num_list)))
