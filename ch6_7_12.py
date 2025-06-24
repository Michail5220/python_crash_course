sarah = {
    'first name': 'sarah',
    'last name': 'johnson',
    'age': '19',
    'city': 'new york'
}

##first_name=sarah.get('first name', 'Unidentified name, please try again...')
#print(f"first name: {first_name.title()}")

#full_name=sarah.get('full name', 'Unidentified name, please try again...')
#print(f"full name: {full_name.title()}")

bob = {
    'first name': 'bob',
    'last name': 'marlou',
    'age': '23',
    'city': 'chicago'
}

dan = {
    'first name': 'dan',
    'last name': 'gibson',
    'age': '33',
    'city': 'nevada'
}

users = [sarah, bob, dan]

for user in users:
        print(f"first name: {user['first name']}\n"
                f"last name: {user['last name']}\n"
                f"age: {user['age']}\n"
                f"city: {user['city']}"
        )

# alternative way

i=0
while i<len(users):
    for user_key, user_value in users[i].items():
        print(f"{user_key} = {user_value}")
    i=i+1


i=0
for i in range(0,len(users),1):
    print(i)



favourite_places = {
     'john': ['jamaica', 'mauritius'],
     'jon': ['jibuti', 'kongo']
}

for person, places in favourite_places.items():
    print(f"Persons name: {person.title()} and his favourite places are: ")
    for place in places:
         print(f"{place.title()}")


vilnius = {'country': 'lithuania', 'population': 600_000, 'fact': 'founded in 14th century'}
tallinn = {'country': 'estonia', 'population': 450_000, 'fact': 'oficially founded in 13th century'}
#doesn't work
#cities = {vilnius, tallinn}


cities = {
     'vilnius': {'country': 'lithuania', 'population': 600_000, 'fact': 'founded in 14th century'},
     'tallinn': {'country': 'estonia', 'population': 450_000, 'fact': 'oficially founded in 13th century'}
}


for city, city_info in cities.items():
     print(f"{city}, country: {city_info['country']}, population: {city_info['population']}")
     #for city_info_key, city_info_data in city_info.items():
     #     print(f"{city_info_key} = {city_info_data}")

     