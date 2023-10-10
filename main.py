from io_interface import IOInterface
from model_user import User
from model_customer import Customer
from model_admin import Admin
from operation_user import UserOperation
from operation_customer import CustomerOperation
from operation_admin import AdminOperation

def login_control():

    IOInterface.main_menu()
    choice = IOInterface.get_user_input("Please enter a number to make your selection: ", 1)
    # login
    if choice[0] == '1':
        logged_in_user = UserOperation.login()
        if logged_in_user is not None:
            if isinstance(logged_in_user, Customer):
                IOInterface.customer_menu(logged_in_user)
            elif isinstance(logged_in_user, Admin):
                IOInterface.admin_menu(logged_in_user)
    # register
    if choice[0] == '2':
        # retrieve username
        while user_name is None:
            user_name = IOInterface.get_user_input("Please enter a username: \n(must include alphabetical letters and underscores (_) only)", 1)
            if not UserOperation.validate_username(user_name):
                print("Invalid Username. Please try entering another.")
                user_name = None
        # retrieve password
        while user_password is None:
            user_password = IOInterface.get_user_input("Please enter a password: \n(must include at least one letter, one number, and 5+ characters)", 1)
            if not UserOperation.validate_password(user_password):
                print("Invalid password. Please try entering another.")
                user_password = None
        # retrieve email
        while user_email is None:
            user_email = IOInterface.get_user_input("Please enter your email address: ", 1)
            if not CustomerOperation.validate_email(user_email):
                print("Invalid email. Please try entering it again.")
                user_email = None
        # retrieve mobile
        while user_mobile is None:
            user_mobile = IOInterface.get_user_input("Please enter your mobile number without spaces.", 1)
            if not CustomerOperation.validate_mobile(user_mobile):
                print("Invalid mobile. Please try entering it again.")
                user_mobile = None

        user_id = UserOperation.generate_user_id()
        user_register_time = UserOperation.retrieve_time_of_registration()

        new_user = Customer(user_id, user_name, user_password, user_register_time, user_email, user_mobile)
        CustomerOperation.register_customer(new_user)

        if new_user is not None:
            IOInterface.customer_menu()
    # exit
    if choice[0] == '3':
        exit()

def customer_control():
    pass


def admin_control():
    IOInterface.admin_menu()
    choice = IOInterface.get_user_input("Please enter a number to make your selection: ", 1)
    if choice[0] == '1':
        print("Show Products logic")
    elif choice[0] == '2':
        print("Add Customers logic")
    elif choice[0] == '3':
        print("Show Customers logic")
    elif choice[0] == '4':
        print("Show Orders logic")
    elif choice[0] == '5':
        print("Generate test data logic")
    elif choice[0] == '6':
        print("Generate all statistical figures logic")
    elif choice[0] == '7':
        print("Delete all data logic")
    elif choice[0] == '8':
        return


def main():
    login_control()

main()