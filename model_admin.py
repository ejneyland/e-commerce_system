from model_user import User
# admin class inherits the User class attributes and methods
class Admin(User):

    # Admin Constructor method
    def __init__(self, user_id, user_name, user_password, user_register_time):
        # id, name, password & time are initialised through the User constructor
        super().__init__(user_id, user_name, user_password, user_register_time)
        # user_role is overwritten from the default "customer"
        self.user_role = "admin"

    # Admin Str Object method
    def __str__(self):
        user_data = {
            'user_id': self.user_id, 
            'user_name': self.user_name, 
            'user_password': self.user_password, 
            'user_register_time': self.user_register_time, 
            'user_role': self.user_role
        }
        return str(user_data)