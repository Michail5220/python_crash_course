

#ch7-4

# message = ""
# toppings=[]
# while message!="quit":
#     prompt = "Please enter a pizza topping (or type 'quit' to stop): "
#     message=input(prompt)
#     if message!="quit":
#         toppings.append(message)


# for topping in toppings:
#     print(f"{topping.title()}\n")

#ch7-5

# ask age
# if under age of three - ticket is free
# if under age of 13 and older than 3 - ticket is $10
# if over 12 ticket is $15

prompt="Please enter the age of a person you're buying the ticket for: "
output_message = "The cost of the ticket: "
rate1=10
rate2=15

message=""
while message != "quit":
    message = input(prompt)
    
    if message!="quit":
        num=int(message)
        if num<3:
            print(f"{output_message}is FREE.")
        elif num<13:
            print(f"{output_message}is ${rate1}.")
        else:
            print(f"{output_message}is ${rate2}.")
    else:
        print("quitting the program!")

