from user import User
class Privileges:
    """writing a separate class that display the administrator priviledges"""
    def __init__(self):
        """initializing a constructor for the privileges class"""
        self.privileges = ["can add post","can delete post","can ban user"]

    def show_privileges(self):
        print("The following are the list of privileges given to the administrator:")
        for privilege in self.privileges:
            print(privilege)

class Admin(User):
    """initializing an admin class that inherit from user's class"""
    def __init__(self,first_name,last_name,user_name,location,age):
        """initializing constructor for the admin class"""
        super().__init__(first_name,last_name,user_name,location,age)
        self.privilegess = Privileges()
