# v=input("tell:")
# print(f"this is what's been said: {v}")

# car = input("What rental car would you like? What make?")
# print(f"Let's see if I can find you a {car.title()}")

# diners_prompt = input("How many people are in your group to reserve a table?")
# diners=int(diners_prompt)

# if diners > 8:
#     print("You cannot go to your table right now. You'd have to wait.")
# else:    
#     print("Your table is ready.")


num_prompt = input("please enter a number and I will tell you whether it is a multiple of ten: ")

num = int(num_prompt)

if num % 10 == 0:
    print("the number is a multiple of ten!")
else:
    print("the number is NOT a multiple of ten")
