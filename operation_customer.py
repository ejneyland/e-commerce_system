class CustomerOperation:
    
    def save_to_file(new_customer):
        # appends a string representation of a new Customer instance to textfile
        user_data = str(new_customer)
        # "a" option to 'append' to the users textfile-database in the data folder
        with open("data/users.txt", "a") as file:
            file.write(user_data + '\n')

    def validate_email(user_email):
        pass # returns True/False

    def validate_mobile():
        pass # returns True/False

    def register_customer(user_name, user_password, user_email, user_mobile):
        pass # returns True/False

    def update_profile(attribute_name, value, customer_object):
        pass # returns True/False

    def delete_customer(customer_id):
        pass # returns True/False

    def get_customer_list(page_number):
        pass # return tuple
        # including a list of customers objects and the total number of pages
        # e.g. ([Customer1, Customer2,...., Customer10], page_number, total_page)

    def delete_all_customers():
        pass # no return