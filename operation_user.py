import random
import datetime
from model_customer import Customer
from model_admin import Admin

class UserOperation:
    
    existing_ids = set()

    @staticmethod
    def generate_user_id():
        # must start with 'u_' followed by 10 digits
        # e.g. 'u_0123456789'
        while True:
            user_id = 'u_' + ''.join(str(random.randint(0, 9)) for _ in range(10))
            # checks that the generated id is not already in the existing_ids
            # if user_id already exists >> loop restarts >> new user_id generated and checked
            if user_id not in UserOperation.existing_ids:
                # adds the uniquely generated id to a list of existing_ids
                UserOperation.existing_ids.add(user_id)
                # if id is unique >> id is returned
                return user_id
    
    @staticmethod
    def retrieve_time_of_registration():
        # returns the current time in format 'DD-MM-YYYY_HH:MM:SS'
        user_register_time = datetime.datetime.now().strftime("%d-%m-%Y_%H:%M:%S")
        return user_register_time
            
    def encrypt_password(user_password):
        # generates random string double the length of user_password
        characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
        generated_random_string = ''.join(random.choice(characters) for _ in range(len(user_password) * 2))
        # combines random string with user_password
        encrypted_password = ""

        # i = 0 >> i = 1 >> i = 2 >> ... >> i 
        for i in range(0, len(user_password)):
            encrypted_password += generated_random_string[i*2:i*2+2] + user_password[i]

        return "^^" + encrypted_password + "$$"

    def decrypt_password(encrypted_password):
        strip_enc_password = ""
        user_password = ""

        # removes the starting '^^' and ending '$$'
        for char in encrypted_password:
            if char != '^' and char != '$':
                strip_enc_password += char

        for i in range(0, len(strip_enc_password)//3):
            user_password += strip_enc_password[i*3+2]
            
        return user_password
    
    @staticmethod
    def check_username_exists(input_username):
        try:
            with open("data/users.txt", "r") as file:
                for line in file:
                    user_data = eval(line)
                    if user_data['user_name'] == input_username:
                        return True
                return False
        except FileNotFoundError:
            print("File not found.")
            return False
        except Exception as e:
            print(f"An error occurred: {e}")
            return False

    @staticmethod    
    def validate_username(user_name):
        # name should only contain letters or underscores
        # length should be at least 5 characters
        # returns True/False
        return user_name.isalpha() or '_' in user_name and len(user_name) >= 5
        # isalpha() checks if all the characters are alphabet letters

    @staticmethod
    def validate_password(user_password):
        # password should contain at least one letter and one number
        # length should be at least 5 characters
        # returns True/False
        has_a_letter = False
        has_a_digit = False

        if len(user_password) >= 5:
            for char in user_password:
                if char.isalpha():
                    has_a_letter = True
                elif char.isdigit():
                    has_a_digit = True

            return has_a_letter and has_a_digit

        return False

    @staticmethod
    def login(user_name, user_password):
        # returns a Cusomer/Admin object
        # verifies the provided users name and password combination against stored user data
        try:
            with open("data/users.txt", "r") as file:
                for line in file:
                    user_data = eval(line)  # Convert the string representation to a dictionary
                    if user_data['user_name'] == user_name and user_data['user_password'] == user_password:
                        if user_data['user_role'] == 'customer':
                            return Customer(
                                user_data['user_name'], 
                                user_data['user_password'],
                                user_data['user_email'],
                                user_data['user_mobile']
                            )
                        elif user_data['user_role'] == 'admin':
                            return Admin(
                                user_data['user_name'], 
                                user_data['user_password'],
                                user_data['user_email'],
                                user_data['user_mobile']
                            )
                return None  # Return None if login fails
        except FileNotFoundError:
            print("File not found.")
            return None
        except Exception as e:
            print(f"An error occurred: {e}")
            return None


# ------------------------------------------------------------


# password = "admin1" # length = 6
# enc_password = UserOperation.encrypt_password(password)
# # print(len(enc_password)) # 22 - 4 = 18 (stripped)
# dec_password = UserOperation.decrypt_password(enc_password)
# print(dec_password) # admin1

# password_two = "FIT9136" # length = 7
# enc_password_two = UserOperation.encrypt_password(password_two)
# print(len(enc_password_two)) # 25 - 4 = 21 (stripped)
# dec_password_two = UserOperation.decrypt_password(enc_password_two)
# print(dec_password_two) # FIT9136
