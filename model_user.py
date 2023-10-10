# rather than importing the UserOperation here
# pass the functions generate_id and retrieve_time 
# as parameters when instantiating, outside of this class 

class User:
    
    # User Constructor method
    def __init__(self, user_id, user_name, user_password, user_register_time):
        self.user_id = user_id
        self.user_name = user_name
        self.user_password = user_password
        # default values set for user_register_time and user_role
        self.user_register_time = user_register_time or "00-00-0000_00:00:00"
        self.user_role = "customer"

    # User Str Object method
    def __str__(self):
        # defines a dictionary of User attributes, key-value pairs
        user_data = {
            'user_id': self.user_id, 
            'user_name': self.user_name, 
            'user_password': self.user_password, 
            'user_register_time': self.user_register_time, 
            'user_role': self.user_role
        }
        # returns a string representation of the User instance/object
        return str(user_data)

# ------------------------------------------------------------