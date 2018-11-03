
print("Position argument")
def sub(a,b):
    print(a-b)
sub(b = 2, a = 10)


print("Default argument")
def dev(n1, n2 = 1):
    print(n1 // n2)
dev(5)


print("Variable length argument")
def add(*n):
    r = 0
    for i in n:
        r += i
    print(r)
add(2,3,4,5)


print("Keyword Variable length argument")
def person(**info):
    for i,j in info.items():
        print("{}: {}".format(i,j))

person(name="mahmoud", age = 24, city = 'giza')