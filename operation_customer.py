class CustomerOperation:
    
    def save_to_file(new_customer):
        # appends a string representation of a new Customer instance to textfile
        user_data = str(new_customer)
        # "a" option to 'append' to the users textfile-database in the data folder
        with open("data/users.txt", "a") as file:
            file.write(user_data + '\n')

