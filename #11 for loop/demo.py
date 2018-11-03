
list = ['mahmoud', 24, 2.1, 1994]

for i in list:
    print(i)

userIn = int(input("Enter Range"))
for i in range(1,userIn+1):
    print(i)


use = int(input("Enter To print Even Numbers"))
for i in range(use, 0, -1):
    if i%2 == 0:
        print(i)