#Python refers to values that cannot change as immutable, an immutable list is a tuple.

#tuples defined by the brackets, but technically, it's the comma ',' that makes a tuple - tuple
breakfastFoods = ('full english', 'omlette', 'toast', 'pancake', 'eggs', 'bacon')

for foodItem in breakfastFoods:
    print(foodItem)

#won't append, because we are using tuples, an immutable list of items
#breakfastFoods.append('sauce')

#the below approach won't work either, because copying a tuple makes a tuple
#updatedBreakfastFoods = breakfastFoods[:]
#updatedBreakfastFoods.append('juice')

updatedBreakfastFoods = [foodItem for foodItem in breakfastFoods]
updatedBreakfastFoods.append("juice")

print ("updated breakfast list now contains")
for foodItem in updatedBreakfastFoods:
    print(foodItem)

#but the updatedBreakfastFoods is not a TUPLE 
#the only way is to reassign items to the TUPLE

updatedBreakfastFoods.clear()

updatedBreakfastFoods = ('full english', 'omlette', 'toast', 'pancake', 'eggs', 'bacon', 'juice', 'fries')
for foodItem in updatedBreakfastFoods:
    print(foodItem)


#if you want to define a typle with one element, you need to include a trailing comma
my_t=(3,)
print(my_t[0])
    