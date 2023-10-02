import random
import datetime
# import json

class User:

    existing_ids = set()

    # default values set for user_register_time and user_role
    def __init__(self, user_id, user_name, user_password, user_register_time = "00-00-0000_00:00:00", user_role = "customer"):
        self.user_id = user_id
        self.user_name = user_name
        self.user_password = user_password
        self.user_register_time = user_register_time
        self.user_role = user_role

        # adds the uniquely generated id to a list of existing ids
        User.existing_ids.add(user_id)

    @classmethod
    def generate_user_id(cls):
        # must start with 'u_' followed by 10 digits
        # e.g. 'u_0123456789'
        while True:
            user_id = 'u_' + ''.join(str(random.randint(0, 9)) for _ in range(10))
            # checks that the generated id is not already in the existing ids
            # if user_id already exists >> loop restarts >> new user_id generated and checked
            if user_id not in cls.existing_ids:
                # if id is unique >> id is returned
                return user_id
    
    @staticmethod
    def retrieve_time_of_registration():
        # returns the current time in format 'DD-MM-YYYY_HH:MM:SS'
        user_register_time = datetime.datetime.now().strftime("%d-%m-%Y_%H:%M:%S")
        return user_register_time

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


newUser = User(User.generate_user_id(), "default", "password", User.retrieve_time_of_registration(), "customer")
newUser.save_to_file()