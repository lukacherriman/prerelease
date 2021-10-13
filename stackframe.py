def h(n):
    print('start h')
    print(1/n)
    print(n)

def g(n):
    print('start g')
    h(n-1)
    print(n)

def f(n):
    print('start f')
    g(n-1)
    print(n)

f(4)