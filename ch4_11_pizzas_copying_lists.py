pizzas = ['margharita', 'hawaian', 'texas', 'tajun chicken', 'pepperoni']

#this is how you copy the list
#friendsPizzas=pizzas would not work, if pizzas would change at any point
#later on, then friendsPizzas would change in the same way.
friendsPizzas = pizzas[:]

friendsPizzas.append("veggie")

x=1
for pizza in friendsPizzas:
    message = f"friends pizza no: {x} is {pizza}."
    print(message)
    x=x+1

print("whereas my pizzas are: ")
print(pizzas)
