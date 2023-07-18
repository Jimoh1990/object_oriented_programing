class User:
    """creating a user class from scratch"""

    def __init__(self, first_name, last_name, user_name, location, age):
        self.first = first_name
        self.last = last_name
        self.u_name = user_name
        self.location = location
        self.age = age
        self.login_attempts = 0

    def describe_user(self):
         """creating a method for the user profile"""
         msg = f"Do you know that {self.first} {self.last} who lives in {self.location} at {self.age} is also called {self.u_name}"
         print(msg)
         print()

    def greet_user(self):
        """creating another method to greet user"""
        msg1 = f"I want to use this medium to greet {self.first} {self.last}"
        print(msg1)
        print()

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0
