#avoid else: clause whenever possible, it is better to account for all possible scenarios in the elif statements,
#thereby avoiding a scenario where a rogue value is executed in the else (catch all) block

car = 'Subaru'
print ("the car is Subaru?")
print(car.lower()=='subaru')

car = 'Subaru'
car = 'Subaru' 
print ("the car is Subaru?")
print(car.lower()=='Subaru')


car = 'Subaru'
print ("is the NOT a Toyota make?")
print(car.lower()!='subaru')

carSpeed = 80
carGear = 4
okToSwitchGear = carSpeed > 70 and carSpeed <= 100 and carGear <5
print(f"Given that speed is: {carSpeed} and the gear is: {carGear} it is ok to switch gear? {okToSwitchGear}")

okToSwitchGear = (carSpeed > 70 and carSpeed <= 100) or (carGear == 3)
print(f"Given that speed is: {carSpeed} and the gear is: {carGear} it is ok to switch gear? {okToSwitchGear}")

collectedItems = ['stamps', 'stickers', 'paintings', 'ceramics']
print('stamps' in collectedItems)

collectedItems = ['stamps', 'stickers', 'paintings', 'ceramics']
print('stamps' not in collectedItems)