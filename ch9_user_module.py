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

# new_user = User('John', 'Bishop', 18, '2007-06-22')
# # other_user = User('Jill', 'Jones', 28, '1997-07-12')
# new_user.describe_user()
# # other_user.describe_user()
# new_user.increment_login_attempts()
# new_user.increment_login_attempts()
# new_user.increment_login_attempts()
# # new_user.reset_login_attempts()
# print(new_user.login_attempts)



# class Priveleges:
#     """Ch9. Ex8. Priveleges"""
#     def __init__(self):
#         self.priveleges=["can read"]

#     def show_priveleges(self):
#         for privelege in self.priveleges:
#             print(privelege)

# # important thing to note, if a parent class is defined below the child class, it won't work!
# class Admin(User):
#     """Ch9. Ex7. Ex8  Admin"""
#     def __init__(self, first_name, last_name, age, dob):
#         super().__init__(first_name, last_name, age, dob)
#         # self.priveleges=[]
#         self.priveleges=Priveleges()
        

#     def show_priveleges(self):
#         for privelege in self.priveleges.priveleges:
#             print(privelege)

