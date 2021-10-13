list1 = [2,5,15,36,47,56,59,78,156,244,268]
list2 = [18,39,42,43,66,69,100]
merge_list =[]

p1 = 0
p2 = 0
while p1 < len(list1) and p2 < len(list2):
    if list1[p1] < list2[p2]:
        merge_list.append(list1[p1])
        p1 += 1
    else:
        merge_list.append(list2[p2])
        p2 +=1
if p1 != len(list1) -1:
    merge_list += list1[p1:]
else:
    merge_list += list2[p2:]

print(merge_list)