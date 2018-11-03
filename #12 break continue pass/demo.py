
stock = 4
user  = int(input("Enter the number you want"))

i= 1
while i <= user:
    if i > stock:
        print("out of stock !!")
        break
    else:
        print("number", i)
    i += 1
print("End of break")

c = int(input("Enter The number to continue"))

for i in range(1, c+1):
    if i%3 == 0:
        continue
    print("number", i)
print("End of continue")

p = int(input("Enter The number to pass"))

for i in range(1, p+1):
    if i%2 != 0:
        pass
    else:
        print(i)
print("End if pass")