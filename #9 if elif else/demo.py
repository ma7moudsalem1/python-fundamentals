
degree = int(input("Enter Your Degree from 0 to 100"))


if degree < 50:
    print("Your grade is F")
elif degree >= 50 and degree < 60:
    print("Your grade is D")
elif degree >= 60 and degree < 75:
    print("Your grade is C")
elif degree >= 75 and degree < 85:
    print("your grade is B")
elif degree >= 85:
    print("Your grade is A")
else:
    print("Enter Valid Number")

