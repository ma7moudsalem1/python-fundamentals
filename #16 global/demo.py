
x = 12

def getNumber():
    global x;
    x = 18
    print("Inside the function:", x)

getNumber()

print("Outside the function", x)


def localAndGlobal():
    a = globals()['x']
    print("local x =", a)
    globals()['x'] = 20

localAndGlobal()
print("S2,Outside the function", x)

