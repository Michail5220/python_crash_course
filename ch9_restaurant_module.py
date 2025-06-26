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

