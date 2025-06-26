class Restaurant:
    """Class describing a restaurant"""
    def __init__(self, name, cuisine_type):
        self.name=name
        self.cuisine_type=cuisine_type
        self.number_served=0
    
    def describe_restaurant(self):
        print(f"Welcome to {self.name} restaurant. We offer a wide range of dishes from the {self.cuisine_type} kitchen.")
    
    def open_restaurant(self):
        print(f"The {self.name} restaurant is currently open.")

    def set_number_served(self,number_served):
        self.number_served=number_served

    def increment_number_served(self,number_served):
        """increment a number of customers served"""
        self.number_served+=number_served


# my_restaurant = Restaurant('German Kebabs', 'German and Turkish')
# my_restaurant.describe_restaurant()
# my_restaurant.open_restaurant()

# competitor_restaurant = Restaurant('A Le Kebabs', 'Kurdish')
# competitor_restaurant.describe_restaurant()
# competitor_restaurant.open_restaurant()

# affiliate_restaurant = Restaurant('Bring me Kebabs', 'Georgian')
# affiliate_restaurant.describe_restaurant()
# affiliate_restaurant.open_restaurant()

my_restaurant = Restaurant('German Kebabs', 'German and Turkish')
my_restaurant.describe_restaurant()
# print(my_restaurant.number_served)
# my_restaurant.number_served=5
# my_restaurant.set_number_served(6)
my_restaurant.increment_number_served(7)
my_restaurant.increment_number_served(8)
print(my_restaurant.number_served)

class User:
    """Class describing a user"""
    def __init__(self, first_name, last_name, age, dob):
        self.first_name=first_name
        self.last_name=last_name
        self.age=age
        self.dob=dob
        self.login_attempts=0

    def describe_user(self):
        print(f"Hi! My name is {self.first_name.title()} {self.last_name.title()}. I am {self.age} and I was born in {self.dob}")

    def increment_login_attempts(self):
        """increment login attempts method"""
        self.login_attempts+=1
    
    def reset_login_attempts(self):
        self.login_attempts=0

new_user = User('John', 'Bishop', 18, '2007-06-22')
# other_user = User('Jill', 'Jones', 28, '1997-07-12')
new_user.describe_user()
# other_user.describe_user()
new_user.increment_login_attempts()
new_user.increment_login_attempts()
new_user.increment_login_attempts()
# new_user.reset_login_attempts()
print(new_user.login_attempts)


class IceCreamStand(Restaurant):
    """Ch9, Ex6. Ice cream stand"""
    def __init__(self, name, cuisine_type):
        super().__init__(name, cuisine_type)
        self.flavours=['Vanilla']

    def show_flavours(self):
        for flavour in self.flavours:
            print(flavour)


ice_shop = IceCreamStand("Ice Cream Shop", "International")
ice_shop.flavours=['Strawberry', 'Chocolate']
ice_shop.describe_restaurant()
ice_shop.show_flavours()


class Priveleges:
    """Ch9. Ex8. Priveleges"""
    def __init__(self):
        self.priveleges=["can read"]

    def show_priveleges(self):
        for privelege in self.priveleges:
            print(privelege)

# my_privelege = Priveleges()
# my_privelege.priveleges=["can write"]
# my_privelege.show_priveleges()

# important thing to note, if a parent class is defined below the child class, it won't work!
class Admin(User):
    """Ch9. Ex7. Ex8  Admin"""
    def __init__(self, first_name, last_name, age, dob):
        super().__init__(first_name, last_name, age, dob)
        # self.priveleges=[]
        self.priveleges=Priveleges()
        

    def show_priveleges(self):
        for privelege in self.priveleges.priveleges:
            print(privelege)

admin_user = Admin("John", "Bishop", 55, 1970)
admin_user.describe_user()
# admin_user - is the instance of the admin class
# priveleges - is the attribute of the admin_user, which is also an instance of the Priveleges class
# priveleges - is the attribute of the Priveleges class
admin_user.priveleges.priveleges=["can read", "can write"]
admin_user.show_priveleges()
