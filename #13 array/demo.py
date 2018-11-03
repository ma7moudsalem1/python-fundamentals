from array import *

arr = array('I', [1,2,3,4,5])
arr.reverse()

print("type one")
for i in arr:
    print(i)

print("type two")
for i in range(len(arr)):
    print(arr[i])

newArr = array(arr.typecode, (e for e in arr))
print("copied array")
for i in range(len(newArr)):
    print(newArr[i])