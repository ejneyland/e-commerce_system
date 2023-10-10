from model_user import User
# customer class inherits the User class attributes and methods
class Customer(User):

    # Customer Constructor method
    def __init__(self, user_id, user_name, user_password, user_register_time, user_email, user_mobile):
        # id, name, password & time are initialised through the User constructor
        # the default user_role "customer" is also inherited, and does not need to be parsed
        super().__init__(user_id, user_name, user_password, user_register_time)
        self.user_email = user_email
        self.user_mobile = user_mobile

    # Customer Str Object method
    def __str__(self):
        user_data = {
            # defines a dictionary of Customer attributes, key-value pair
            'user_id': self.user_id, 
            'user_name': self.user_name, 
            'user_password': self.user_password, 
            'user_register_time': self.user_register_time, 
            'user_role': self.user_role,
            'user_email': self.user_email,
            'user_mobile': self.user_mobile
        }
        return str(user_data)

# ------------------------------------------------------------