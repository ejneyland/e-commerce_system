# rather than importing the UserOperation here
# pass the functions generate_id and retrieve_time 
# as parameters when instantiating, outside of this class 

class User:
    # default values set for user_register_time and user_role
    # user_id, user_register_time and user_role are fields determined by static
    # methods and not from user input, so they are not in the constructor params
    def __init__(self, user_id, user_name, user_password, user_register_time):
        self.user_id = user_id
        self.user_name = user_name
        self.user_password = user_password
        self.user_register_time = user_register_time or "00-00-0000_00:00:00"
        self.user_role = "customer"

    def __str__(self):
        # returns a string representation of the User instance/object
        # contains key-value pairs for all attributes
        user_data = {
            'user_id': self.user_id, 
            'user_name': self.user_name, 
            'user_password': self.user_password, 
            'user_register_time': self.user_register_time, 
            'user_role': self.user_role
        }
        return str(user_data)

# ------------------------------------------------------------

# ethan = User("the_lizzard_king", "password123")
# print(str(ethan))
