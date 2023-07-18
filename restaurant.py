class Restaurant:
    """initiating a restaurant class"""

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f"\nThe restaurant name is {self.restaurant_name}")
        print(f"The cuisine type is {self.cuisine_type}")
        print(f"{self.restaurant_name} has served {self.number_served} persons")

    def open_restaurant(self):
        print(f"\n{self.restaurant_name} is now open")

    def set_number_served(self, number_served):
        self.change_served = number_served
        print(f"The numbers of people served is now {self.change_served}")

    def increament_number_served(self, number_served):
        self.number_served += number_served
        print(f"The new number served is {number_served}")

class IceCreamStand(Restaurant):
    """writing a class that inherit from Restaurant"""
    def __init__(self,restaurant_name,cuisine_type):
        super().__init__(restaurant_name,cuisine_type)
        self.flavour = ["sweet_icecream", "sour_icecream"]

    def display_flavours(self):
        for cream in self.flavour:
            print(cream.title())

my_stand = IceCreamStand("mamaB","chill")
my_stand.display_flavours()
