#7-8
# sandwich_orders = ['salami', 'ham', 'cheese', 'ham&cheese']
# finished_sandwiches = []

# for sandwich in sandwich_orders:
#     print(f"I've made a {sandwich} sandwich!")
#     finished_sandwiches.append(sandwich)
# print("\nA list of finished sandwiches:")
# for sandwich in finished_sandwiches:
#     print(f"{sandwich.upper()}")

#7-9
# sandwich_orders = ['pastrami','salami', 'ham', 'pastrami','cheese', 'ham&cheese', 'pastrami']
# finished_sandwiches = []

# print("The deli ran out of pastrami sandwiches!")

# while 'pastrami' in sandwich_orders:
#     sandwich_orders.remove('pastrami')

# for sandwich in sandwich_orders:
#     print(f"I've made a {sandwich} sandwich!")
#     finished_sandwiches.append(sandwich)
# print("\nA list of finished sandwiches:")
# for sandwich in finished_sandwiches:
#     print(f"{sandwich.upper()}")

#7-10
#prompt a place to visit 
#add a place to visit to a dictionary, and add poll_value to 1
#do this for each new place
#for existing place in the dictionary, increase poll_value

new_place=''
places_to_visit = {}
flag = True

while flag:
    new_place = input("Please enter a your dream place to visit: ")
    if new_place != 'quit':
    
        if new_place not in places_to_visit.keys():
            print("yes")
            places_to_visit[new_place]=1
        else:
            val = places_to_visit.get(new_place)+1
            places_to_visit.update({new_place: val})
            #or
            #places_to_visit[new_place]=val
        
        print(places_to_visit)
    else:
        flag = False
        print("quitting the program")

print(places_to_visit)