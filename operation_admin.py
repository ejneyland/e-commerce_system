class AdminOperation:
    
    # def register_admin():
    def save_to_file(new_admin):
        # appends string representation of a new Admin instance to textfile
        user_data = str(new_admin)
        # "a" option to 'append' to the users textfile-database in the data folder
        with open("data/users.txt", "a") as file:
            file.write(user_data + '\n')