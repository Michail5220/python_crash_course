from ch9_user_module import User

class Priveleges:
    """Ch9. Ex8. Priveleges"""
    def __init__(self):
        self.priveleges=["can read"]

    def show_priveleges(self):
        for privelege in self.priveleges:
            print(privelege)

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

