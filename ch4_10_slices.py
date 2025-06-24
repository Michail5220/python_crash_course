mammals=['bears', 'dogs', 'wolves', 'lions', 'tigers']

#python stops before 1 item you specify
#print items 0 to 3 Inclusive
print(mammals[0:3])
#equivalent notation
print(mammals[:3])
print("three items from the middle of the list are:")
print(mammals[2:4]) #returns wolves and lions
print("the last three items in the list are:")
print(mammals[-3:])
#for items 1 to 5 inclusive, choose every second one
print(mammals[0:5:2])   #returns bears, wolves, tigers