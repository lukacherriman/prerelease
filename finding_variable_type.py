from sys import getsizeof
test_var = set()
for i in range(100):
    print(test_var, getsizeof(test_var))
    test_var.add(i)
