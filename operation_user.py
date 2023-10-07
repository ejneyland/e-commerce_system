import random
import datetime

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
                    else:
                        return False
        except FileNotFoundError:
            print("File not found.")
            return False
        except Exception as e:
            print(f"An error occurred: {e}")
            return False
        
    def validate_username(user_name):
        pass # returns True/False

    def validate_password(user_password):
        pass # returns True/False

    def login(user_name, user_password):
        pass # returns a Cusomer/Admin object


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
