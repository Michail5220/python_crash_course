alien_color = 'red'

if alien_color=='green':
    print('You earned 5 points!')
else:
    print("You haven't earned anything!")


#5-4
alien_color = 'red'

if alien_color=='green':
    print('You earned 5 points!')
else:
    print("You have earned 10 points!")

if alien_color=='green':
    print('You earned 5 points!')
if alien_color!='green':
    print("You have earned 10 points!")


#5-5

alien_color='green'

if alien_color=='green':
    print('You have earned 5 points!')
elif alien_color=='yellow':
    print('You have earned 10 points!')
elif alien_color=='red':
    print('You have earned 15 points!')
else:
    print('Don\'t recognise this color')


if alien_color == 'green':
    print('You have earned 5 points!')
if alien_color == 'yellow':
    print('You have earned 10 points!')
if alien_color == 'red':
    print('You have earned 15 points!')


#5-6
age = 83
person = "unknown"

if age < 2:
    person = "baby"
elif age < 4:
    person = "toddler"
elif age < 13:
    person = "kid"
elif age < 20: 
    person = "teenager"
elif age < 65:
    person = "adult"
elif age >= 65:
    person = "an elder"

print("this person is a " + person)

#5-7

favourite_fruits = ['apple', 'banana', 'orange']
fruit = "pineapple"

if fruit in favourite_fruits:
    print(f"you really like {fruit}")
else:
    print(f"you really don't like {fruit}")


#5-8

print("usernames task!")
usernames = ["Finlay", "Jonathan", "Admin"]

if usernames:
    for user in usernames:
        if user == "Admin":
            print("Hello admin, would you like to see the status report?")
        else: 
            print(f"Hello {user}, thank you for logging in again.")
else:
    print("sorry, you need to register first")


#5-10
    
print("CHECKING USERNAMES!")

current_users= ["John", "Michael", "Robert"]
new_users = ["Craig", "Michael"]

current_users_lower = current_users[:]
i = 0
for current_user in current_users_lower:
    current_users_lower[i] = current_users_lower[i].lower()
    i=i+1

print(current_users_lower)

for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print("enter a new username")
    else:
        print("the username is available")


#5-11
print("ORDINAL NUMBERS!")

numbers = range(1,10)
str_numbers = []
suffix = "st"
for num in numbers:
    if num == 1:
        suffix='st'
    elif num == 2:
        suffix='nd'
    elif num == 3:
        suffix='rd'
    else:
        suffix='th'
    str_numbers.append(f"{str(num)}{suffix}")

for str_num in str_numbers:
    print(str_num)

