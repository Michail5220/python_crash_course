
# add an element to the list (end of the list)
# list_name.append('some_value') 
# 
# insert element into a given position
# list_name.insert(0,'some_value')
#
# remove an element from a given position
# del list_name[0]
#
# remove last element in the list
# popped_element = list_name.pop()
# OR from a given position
# popped_element = list_name.pop(0)
#
# removing by value
# list_name.remove('some_value')

invitees = ['John', 'Michael', 'Jimmy', 'Richard']
message = "you're invited to Dinner"
print(f"{invitees[0]} {message}!")
print(f"{invitees[1]} {message}!")
print(f"{invitees[2]} {message}!")
print(f"{invitees[-1]} {message}!")

unable_to_attend = invitees.pop(1); 
#if pop() is used without the parameter, the last element in the list will be dropped
print("There is a person who is unable to attend: " + unable_to_attend )

print(f"{invitees[0]} {message}!")
print(f"{invitees[1]} {message}!")
print(f"{invitees[2]} {message}!")

print("more people attending, a bigger table has been found!")
invitees.insert(0,'Alex')
invitees.insert(1,'Sean')
invitees.append('David')

print(f"{invitees[0]} {message}!")
print(f"{invitees[1]} {message}!")
print(f"{invitees[2]} {message}!")
print(f"{invitees[3]} {message}!")
print(f"{invitees[4]} {message}!")
print(f"{invitees[5]} {message}!")

cancelled_invitee = invitees.pop();
print("Sorry " + cancelled_invitee + ", the invitation has been cancelled due to restaurant's table is unavailable")
cancelled_invitee = invitees.pop();
print("Sorry " + cancelled_invitee + ", the invitation has been cancelled due to restaurant's table is unavailable")
cancelled_invitee = invitees.pop();
print("Sorry " + cancelled_invitee + ", the invitation has been cancelled due to restaurant's table is unavailable")
cancelled_invitee = invitees.pop();
print("Sorry " + cancelled_invitee + ", the invitation has been cancelled due to restaurant's table is unavailable")

print(f"{invitees[0]} {message}!")
print(f"{invitees[1]} {message}!")

del invitees[0]
del invitees[1]

