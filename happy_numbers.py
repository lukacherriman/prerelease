global happy
happy = False

def happy_number(n):
    global happy
    if n == 1:
        happy = True
        return
    elif n != 1:
        digs = []
        for i in str(n):
            digs.append(int(i))
        n = 0
        for i in range(len(digs)):
            n += digs[i] ** 2
        if n == 4:
            return
        happy_number(n)




happy_number(4)
print(happy)