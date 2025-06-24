wish_locations = ['bulgaria','scotland','malta', 'croatia', 'spain']
print(wish_locations)
#sorted method only does it temporarily and doesn't change the actual
#order in the wish_locations list
print(sorted(wish_locations))
print(wish_locations)
#sorted function can take another parameter, reverse=True, 
#self-explanatory here...
print(sorted(wish_locations,reverse=True))
print(wish_locations)
#reverse method reverses the order of the list permanently, however,
#run the method again to reverse back to the original order
wish_locations.reverse()
print(wish_locations)
wish_locations.reverse()
print(wish_locations)
#unlike sorted function, sort method does it permanently
wish_locations.sort();
print(wish_locations)
wish_locations.sort(reverse=True)
print(wish_locations)
print(len(wish_locations))
