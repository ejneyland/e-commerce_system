from model_customer import Customer
from operation_user import UserOperation

class CustomerOperation(UserOperation):

    def validate_email(user_email):
        # checks if '@' and '.' are present in the email
        if '@' in user_email and '.' in user_email:
        # splits the email into username and domain parts
            username, domain = user_email.split('@')
        
            # checks username length
            if len(username) >= 3:
                # splits the domain into domain name and top-level domain
                domain_name, top_level_domain = domain.split('.')
                
                # checks the domain name length and top-level domain length e.g. gmail.com
                if len(domain_name) >= 2 and len(top_level_domain) >= 2:
                    return True
        return False

    def validate_mobile(user_mobile):
        return len(user_mobile) == 10 and (user_mobile.startswith("04") or user_mobile.startswith("03"))

    def register_customer(user_id, user_name, user_password, user_email, user_mobile, user_register_time):
        # must include
        # apply validations on all the values
        # if the user_name exists in textfile return False
        # unique user_id required when registering new user
        # user_register_time
        # returns True/False
        # appends a string representation of a new Customer instance to textfile
        if CustomerOperation.check_username_exists(user_name):
            return False
        user_data = str(Customer(user_name, user_password, user_email, user_mobile, user_register_time))
        # "a" option to 'append' to the users textfile-database in the data folder
        with open("data/users.txt", "a") as file:
            file.write(user_data + '\n')
        return True

    def update_profile(attribute_name, value, customer_object: Customer):
        if attribute_name == "user_name":
            customer_object.user_name = value
        elif attribute_name == "user_password":
            customer_object.user_password = value
        elif attribute_name == "user_email":
            customer_object.user_email = value
        elif attribute_name == "user_mobile":
            customer_object.user_mobile = value
        return customer_object

    def delete_customer(customer_id):
        lines = []
        deleted = False
        with open("data/users.txt", "r") as file:
            lines = file.readlines()

        with open("data/users.txt", "w") as file:
            for line in lines:
                if line.strip().split(',')[0] != customer_id:
                    file.write(line)
                else:
                    deleted = True
        return deleted

    def get_customer_list(page_number):
        pass 
        with open("data/users.txt", "r") as file:
            customers = []
            users = [line.strip().split(',') for line in file]
            start_index = (page_number - 1) * 10
            end_index = min(page_number * 10, len(customers))
            return customers[start_index:end_index], page_number, len(customers) // 10 + 1

    def delete_all_customers():
        with open("data/users.txt", "r") as file:
            lines = file.readlines()

        with open("data/users.txt", "w") as file:
            for line in lines:
                if line.strip().split(',')[4] == 'customer':
                    file.write(line)