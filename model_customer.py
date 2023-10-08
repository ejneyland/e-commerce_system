from model_user import User

class Customer(User):

    def __init__(self, user_name, user_password, user_email, user_mobile):
        # user_id, user_register_time and user_role 
        # automatically generated through the User constructor
        super().__init__(user_name, user_password)
        self.user_email = user_email
        self.user_mobile = user_mobile

    def __str__(self):
        user_data = {
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

# steve = Customer(user_name="stevey_boi", user_password="steve123", user_email="stevey@gmail.com", user_mobile="1800 STEVE")

# CustomerOperation.save_to_file(steve)

# emma = Customer(user_name="emma_mc'ween", user_password="password", user_email="emma@gmail.com", user_mobile="1800 EMMA")

# CustomerOperation.save_to_file(emma)