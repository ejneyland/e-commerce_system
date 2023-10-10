import random
import datetime
from model_order import Order
from model_customer import Customer
from operation_customer import CustomerOperation

class OrderOperation:
    
    existing_ids = set()

    @staticmethod
    def generate_order_id():
    # def generate_unique_order_id():
        while True:
            order_id = 'o_' + ''.join(str(random.randint(0, 9)) for _ in range(5))
            # checks that the generated id is not already in the existing_ids
            # if prod_id already exists >> loop restarts >> new prod_id generated and checked
            if order_id not in OrderOperation.existing_ids:
                # adds the uniquely generated id to the list of existing_ids
                OrderOperation.existing_ids.add(order_id)
                # if id is unique >> id is returned
                return order_id

    @staticmethod
    def retrieve_time_of_order():
        # returns the current time in format 'DD-MM-YYYY_HH:MM:SS'
        order_time = datetime.datetime.now().strftime("%d-%m-%Y_%H:%M:%S")
        return order_time
    
    def create_an_order(customer_id, product_id):
        order_id = OrderOperation.generate_order_id()
        time_of_order = OrderOperation.generate_random_time_of_order()

        order_data = f"{order_id},{customer_id},{product_id},{time_of_order}\n"

        with open("data/orders.txt", "a") as file:
            file.write(order_data)

        return True


    def delete_order(order_id):
        deletion_successful = False
        with open("data/orders.txt", "r") as file:
            lines = file.readlines()

            for line in lines:
                if line.strip().split(',')[0] == order_id:
                    lines.remove(line)
                    deletion_successful = True

        with open("data/orders.txt", "w") as file:
            file.writelines(lines)
        
        return deletion_successful
    
    def delete_all_orders():
        with open("data/orders.txt", "w") as file:
            file.write("")

    def get_order_list(customer_id, page_number):
        with open("data/orders.txt", "r") as file:
            orders = [line.strip().split(',') for line in file]
            start_index = (page_number - 1) * 10
            end_index = min(page_number * 10, len(orders))
            return orders[start_index:end_index], page_number, len(orders) // 10 + 1

    # ------------

    def generate_test_order_data():
        # 10 customer names
        names = ["John Doe", "Jane Smith", "Michael Johnson", "Sara Brown", "David Lee", "Laura Davis", "Daniel Wilson", "Emma Evans", "James Taylor", "Olivia Miller"]

        # create a customer instance for all 10 customer names
        for name in names:
            user_id = CustomerOperation.generate_user_id()
            user_name = name
            # this constructor will create the same password, email, and mobile for each Customer instance for simplicity
            user_password = "password123"
            user_register_time = "00-00-0000_00:00:00"
            user_email = "customer@gmail.com"
            user_mobile = "0419 123 456"
            CustomerOperation.register_customer(user_id, user_name, user_password, user_register_time, user_email, user_mobile)

            # create customer orders for each customer
            no_of_orders = random.randint(50, 200)
            product_ids = OrderOperation.get_product_ids()

            for _ in range(no_of_orders):
                product_id = random.choice(product_ids)
                OrderOperation.create_an_order(user_id, product_id)
    
    def get_product_ids():
        with open("data/products.txt", "r") as file:
            products = [line.strip().split(',')[-2] for line in file]
        return products
    
    # generates a random date and time across years 2022 and 2023
    def generate_random_time_of_order():
        year = random.randint(2022, 2023)
        month = random.randint(1, 12)
        day = random.randint(1, 28)
        hour = random.randint(0, 23)
        minute = random.randint(0, 59)
        second = random.randint(0, 59)

        return f"{day:02d}-{month:02d}-{year}_{hour:02d}:{minute:02d}:{second:02d}"

    def generate_single_customer_consumption_figure(customer_id):
        pass
    # generate a graph to show the cosumption (sum of order price) of 12 different months for the given customer

    def generate_all_customer_consumption_figure():
        pass
    # generates a graph to show the cosumption (sum of order price) of 12 different months for all customers

    def generate_all_top_10_best_sellers_figure():
        pass
    # generates a graph showing the top 10 best selling products and sort the result in descending order
