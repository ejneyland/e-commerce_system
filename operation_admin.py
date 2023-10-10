from model_admin import Admin

class AdminOperation:
    
    @staticmethod
    def register_admin(user_id, user_name, user_password, user_register_time):
        # upon running the application, user database is cleared
        # before being repopulated
        # then, call the register_admin to create single admin instance
        admin = Admin(user_id, user_name, user_password, user_register_time)
        admin_data = str(admin)
        # "a" option to 'append' to the users textfile database
        with open("data/users.txt", "a") as file:
            file.write(admin_data + '\n')