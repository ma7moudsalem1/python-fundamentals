


try:
    x = int(input("Enter First number"))
    y = int(input("Enter Second number"))
    print(x/y)
except ZeroDivisionError as e:
    print("Ops,you can't division by zero it gives you an error",e)
except ValueError as e:
    print("Inter valid number, it gives you an error", e)
except Exception as e:
    print("Ops, Something went wrong")
finally:
    print("end case")
print("End Program")
