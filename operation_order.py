import random
import datetime

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
            
    def create_an_order(customer_id, product_id, create_time):
        pass
        # order data saved into the data/orders.txt
        # returns True/False

    @staticmethod
    def retrieve_time_of_order():
        # returns the current time in format 'DD-MM-YYYY_HH:MM:SS'
        order_time = datetime.datetime.now().strftime("%d-%m-%Y_%H:%M:%S")
        return order_time
    
    def create_an_order(customer_id, product_id):
        order_id = OrderOperation.generate_order_id()
        get_time = OrderOperation.retrieve_time_of_order()

        order_data = f"{order_id},{customer_id},{product_id},{get_time}\n"

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
        pass

    def generate_single_customer_consumption_figure(customer_id):
        pass

    def generate_all_customer_consumption_figure():
        pass

    def generate_all_top_10_best_sellers_figure():
        pass
