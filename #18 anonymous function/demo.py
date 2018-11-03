
r = lambda n : n * n

result = r(2)
print(result)


l = [1,2,3,4,5,6,7,8]

even = list(filter(lambda e : e % 2 == 0, l))
print(even)

double = list(map(lambda e : e * e, even))
print(double)