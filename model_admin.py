from model_user import User

class Admin(User):

    def __init__(self, user_name, user_password):
        super().__init__(user_name, user_password)
        self.user_role = "admin"

    def __str__(self):
        user_data = {
            'user_id': self.user_id, 
            'user_name': self.user_name, 
            'user_password': self.user_password, 
            'user_register_time': self.user_register_time, 
            'user_role': self.user_role
        }
        return str(user_data)