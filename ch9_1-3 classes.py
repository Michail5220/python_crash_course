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
        