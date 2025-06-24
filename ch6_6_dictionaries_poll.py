people_taking_toll = ['Jen', 'Sarah', 'Edward', 'Phil', 'George', 'Caleb']

favourite_languages = {
    'jen':'python',
    'sarah':'c',
    'edward':'rust',
    'phil':'python'
}


for name in people_taking_toll:
    if name.lower() not in favourite_languages.keys():
        print(f"{name.title()} please take the toll!")

# all of the dictionaries in the list should have identical structure,
# so you can loop through the list and work with each dictionary object
# in the same way.

#one way to break up a string
print("this is a string "
    "that consists of three rows "
    "in the code but one in the output")