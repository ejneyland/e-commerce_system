from model_user import User

class Admin(User):

    def __init__(self, user_id, user_name, user_password, user_register_time="00-00-0000_00:00:00", user_role="admin"):
        super().__init__(user_id, user_name, user_password, user_register_time, user_role)

    def __str__(self):
        user_data = {
            'user_id': self.user_id, 
            'user_name': self.user_name, 
            'user_password': self.user_password, 
            'user_register_time': self.user_register_time, 
            'user_role': self.user_role
        }
        return str(user_data)
    
    def save_to_file(self):
        # appends string representation of a new Admin instance to textfile
        user_data = str(self)
        # "a" option to 'append' to the users textfile-database in the data folder
        with open("data/users.txt", "a") as file:
            file.write(user_data + '\n')