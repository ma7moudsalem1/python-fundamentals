
def greet():
    print("Hello all !!")

greet()

def add(n1, n2):
    return n1 + n2

def sub(n1, n2):
    return n1 - n2

def mul(n1, n2):
    return n1 * n2
def dev(n1, n2):
    return n1 // n2

a = add(2,3)
s = sub(6,1)
m = mul(5,1)
d = dev(a,s)
print("Add", a)
print("Sub", s)
print("Mul", m)
print("Dev", d)


print("return more than one value values")
def subAndAdd(n1, n2):
    s = n1 - n2
    a = n1 + n2
    return s,a

s,a = subAndAdd(10, 5)

print("add:", a)
print("Sub", s)