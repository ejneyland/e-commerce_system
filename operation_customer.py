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

    def register_customer(user_id, user_name, user_password, user_register_time, user_email, user_mobile):
        # registration fails if the username already exists
        if CustomerOperation.check_username_exists(user_name):
            return False
        customer = Customer(user_id, user_name, user_password, user_register_time, user_email, user_mobile)
        # appends the new Customer/User to the users database
        with open("data/users.txt", "a") as file:
            file.write(str(customer) + '\n')
        return True

    def update_profile(attribute_name, value, customer_object: Customer):
        # updates/mutates specified user attributes with a new value
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
        # reads each line from the user database
        with open("data/users.txt", "r") as file:
            lines = file.readlines()
        # writes all users to database except for the specified customer for deletion
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
            customers = [line.strip().split(',') for line in file if line.strip().split(',')[4] != 'admin']
            start_index = (page_number - 1) * 10
            end_index = min(page_number * 10, len(customers))
            print(customers[start_index:end_index], page_number, len(customers) // 10 + 1)

    def delete_all_customers():
        with open("data/users.txt", "r") as file:
            lines = file.readlines()

        with open("data/users.txt", "w") as file:
            for line in lines:
                if line.strip().split(',')[4] == 'admin':
                    file.write(line)