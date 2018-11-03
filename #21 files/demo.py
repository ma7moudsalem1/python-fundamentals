
file = open('read', 'r')
print(file.read())


file2 = open('write', 'w')
file2.write("Something")

file2 = open('append', 'a')
file2.write("Something")

image  = open('image.jpg', 'rb')
image2 = open('copy.jpg', 'wb')
for i in image:
    image2.write(i)