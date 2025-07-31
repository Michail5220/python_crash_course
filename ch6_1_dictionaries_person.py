person_a={
    'first name': 'John',
    'last name': 'Bishop',
    'age': 42,
    'city': 'Lincoln'
    }


person_b={
    'first name': 'Leo',
    'last name': 'DeCaprio',
    'age': 40,
    'city': 'LA'
    }


person_c={
    'first name': 'Al',
    'last name': 'Pacino',
    'age': 70,
    'city': 'New York'
    }

people = [person_a, person_b, person_c]


for person in people:
    print(f"This is {person['first name'].title()} {person['last name'].title()} and his details are as follows:")
    print(f"Age: {person['age']}"
          f"\nBirth place: {person['city']}\n")   #note how the line is broken



# print(person_a)
# print(person_a['first name'])
# print(person_a['age'])

# we loop through all the KEYS here, without using .keys() or items() methods
#for key in person_a:
#    print(key)

# equivalent
# for key in person_a:
#    print(key)

rivers = {
    'nemunas': 'lithuania',
    'neris': 'lithuania',
    'sesupe': 'lithuania',
    'wye': 'england',
    'exe': 'england',
    'thames': 'england'
    }
print("\n")
for river, country in rivers.items():
    print(f"The {river.title()} river runs through {country.title()}.")
print("\n")
for country in set(rivers.values()):
    print(f"{country.title()} is a country in our list.")

for country in sorted(set(rivers.values())):
    print(f"{country.title()} is a country in our list.")



#dictionaries inside the list
people = [person_a, person_b, person_c]


for person in people:
    print(f"This is {person['first name'].title()} {person['last name'].title()} and his details are as follows:")
    print(f"Age: {person['age']}"
          f"\nBirth place: {person['city']}\n")   #note how the line is broken


#list inside the dictionary
favourite_places = {
    'joHn':['Vilnius','Warsaw','Tallinn'],
    'Matthew':['London','Sydney','Edinburgh'],
    'Jill':['Blackpool']
    }
print("\t\n")
for person, places in favourite_places.items():
    print(f"{person.title()} likes the following cities:")
    for place in places:
        print(f"{place.title()}")
    print("\n")


#dictionary inside the dictionary

cities = {
    'Vilnius':{
              'country':'Lithuania',
              'population': 544386,
              'fun fact':'The city is one of the few capitals in the world that allows hot air balloons to fly over it, which has become a popular activity that offers unique views'
              },
    'Edinburgh':{
              'country':'Scotland',
              'population':	558676,
              'fun fact':'Edinburgh Castle is built on an extinct volcano'
              }
    }

for city, facts in cities.items():
    print(f"{city.title()} is a capital of {facts['country']} with the population of {facts['population']}.\n")
    print(f"fun fact about {city.title()}: {facts['fun fact']}!\n")
