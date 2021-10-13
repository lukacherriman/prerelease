def permutation(list):
    if len(list) == 1:
        return [list]

    permutations = []
    for i in range(len(list)):
        m = list[i]
        remList = list[:i] + list[i + 1:]
        for p in permutation(remList):
            permutations.append([m] + p)
    return permutations


print(permutation([1,2]))