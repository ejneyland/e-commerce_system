from io_interface import IOInterface
from model_user import User
from model_customer import Customer
from model_admin import Admin
from model_product import Product
from model_order import Order
from operation_user import UserOperation
from operation_customer import CustomerOperation
from operation_admin import AdminOperation
from operation_product import ProductOperation
from operation_order import OrderOperation  

def register():
    while True:
        # retrieve username
        user_name = input("Please enter a username: ")
        if UserOperation.validate_username(user_name):
            break
        else:
            print("Invalid Username. Please try entering another.")
    
    while True:
        # retrieve password
        print("Create password..")
        print("must include at least one letter, one number, and be 5+ characters")
        user_password = input("enter password:  ")
        if UserOperation.validate_password(user_password):
            break
        else:
            print("Invalid password. Please try entering another.")
    
    while True:
        # retrieve email
        user_email = input("Please enter your email address: ")
        if CustomerOperation.validate_email(user_email):
            break
        else:
            print("Invalid email. Please try entering it again.")
    
    while True:
        # retrieve mobile
        user_mobile = input("Please enter your mobile number without spaces:  ")
        if CustomerOperation.validate_mobile(user_mobile):
            break
        else:
            print("Invalid mobile. Please try entering it again.")

    user_id = UserOperation.generate_user_id()
    user_register_time = UserOperation.retrieve_time_of_registration()
    customer = Customer(user_id, user_name, user_password, user_register_time, user_email, user_mobile)

    CustomerOperation.register_customer(user_id, user_name, user_password, user_register_time, user_email, user_mobile)

    return customer

def menu_selection():
    # displays the main menu options
    IOInterface.main_menu()
    available_choices = ["1", "2", "3"]
    while True:
        # asks user for a selection
        choice = input("Please enter a number to make your selection: ")
        if choice in available_choices:
            return choice
        else:
            print("Invalid choice. Please try again.")

def login_control():
    while True:
        user_name = input("Please enter your username:  ")
        if UserOperation.check_username_exists(user_name):
            break
        else: 
            print("Username not found. Please try again.")

    while True:
        user_password = input("Please enter your password:  ")
        logged_in_user = UserOperation.login(user_name, user_password)
        
        if logged_in_user is not None:
            print(f"Welcome, {user_name}!")
            return logged_in_user
        else:
            print("Incorrect password. Please try again.")

def customer_control(customer):
    IOInterface.customer_menu()
    choice = IOInterface.get_user_input("Please enter a number to make your selection: ", 1)
    if choice[0] == '1':    # show profile
        print(str(customer))
    elif choice[0] == '2':  # update profile
        attribute_name = input("Enter the attribute name you want to update (user_name, user_password, user_email, user_mobile): ")
        value = input("Enter the new value: ")
        CustomerOperation.update_profile(attribute_name, value, customer)
        print("Profile updated successfully!")
    elif choice[0] == '3':  # show products
        print("")
    elif choice[0] == '4':  # show order history
        orders = OrderOperation.get_order_history(customer.user_id)
        if orders:
            for order in orders:
                print(str(order))
        else:
            print("No order history available.")
    elif choice[0] == '5':  # generate all consumption figures
        print("Generate all consumption figures")
    elif choice[0] == '6':  # logout
        user = None
        return user

def admin_control():
    IOInterface.admin_menu()
    choice = IOInterface.get_user_input("Please enter a number to make your selection: ", 1)
    if choice[0] == '1': # show products
        IOInterface.products_menu()
        category = IOInterface.get_user_input("Enter a number to display products from a category: ", 1)
        ProductOperation.show_category_products(category[0])
    elif choice[0] == '2': # add customers
        print("Add Customers")
        register()
    elif choice[0] == '3': # show customers
        print("Show Customers")
        CustomerOperation.get_customer_list(1)
    elif choice[0] == '4': # show orders
        print("Show Orders")
        OrderOperation.get_order_list(1)
    elif choice[0] == '5':
        print("Generate test data")
    elif choice[0] == '6':
        print("Generate all statistical figures logic")
    elif choice[0] == '7': # delete all data
        OrderOperation.delete_all_orders()
        ProductOperation.delete_all_products()
        CustomerOperation.delete_all_customers()
    elif choice[0] == '8':
        return

def main():
    # clears the database
    OrderOperation.delete_all_orders()
    ProductOperation.delete_all_products()
    CustomerOperation.delete_all_customers()
    # creates admin instance
    AdminOperation.register_admin("u_0123456789", "admin", "tops3cr3t", "00-00-0000_00:00:00")
    # extracts products, creates customers, creates orders
    ProductOperation.extract_products_from_files()
    OrderOperation.generate_test_order_data()
    # login
    choice = menu_selection()

    if choice == '1':
        print("LOGIN")
        user = login_control()
        if isinstance(user, Customer):
            customer_control(user)
        elif isinstance(user, Admin):
            admin_control()
            
    elif choice == '2':
        print("REGISTER")
        user = register()
        if isinstance(user, Customer):
            customer_control(user)
        elif isinstance(user, Admin):
            admin_control()

main()