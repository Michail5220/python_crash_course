cubeList = []
for value in range(1,11):
    cubeList.append(value ** 3)

print(cubeList);

#list comprehensions, same as above
cubeList2 = [value ** 3 for value in range(1,11)]
print(cubeList2)