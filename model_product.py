import random

class Product:

    existing_ids = set()

    @classmethod
    def generate_prod_id(cls):
        # must start with 'u_' followed by 10 digits
        # e.g. 'u_0123456789'
        while True:
            prod_id = 'p_' + ''.join(str(random.randint(0, 9)) for _ in range(10))
            # checks that the generated id is not already in the existing_ids
            # if prod_id already exists >> loop restarts >> new prod_id generated and checked
            if prod_id not in cls.existing_ids:
                # adds the uniquely generated id to the list of existing_ids
                cls.existing_ids.add(prod_id)
                # if id is unique >> id is returned
                return prod_id
    
    def __init__(self, prod_model, prod_category, prod_name, prod_current_price, prod_raw_price, prod_discount, prod_likes_count):
        self.prod_id = self.generate_prod_id(), 
        self.prod_model = prod_model, 
        self.prod_category = prod_category, 
        self.prod_name = prod_name, 
        self.prod_current_price = prod_current_price, 
        self.prod_raw_price = prod_raw_price, 
        self.prod_discount = prod_discount, 
        self.prod_likes_count = prod_likes_count

    def __str__(self):
        prod_data = {
            'prod_id': self.prod_id, 
            'prod_model': self.prod_model, 
            'prod_category': self.prod_category, 
            'prod_name': self.prod_name,
            'prod_current_price': self.prod_current_price, 
            'prod_raw_price': self.prod_raw_price, 
            'prod_discount': self.prod_discount, 
            'prod_likes_count': self.prod_likes_count
        }

        return str(prod_data)
    
    def save_to_file(self):
        # appends the string representation of a new Product instance to a textfile
        prod_data = str(self)
        # "a" option to 'append' to the prods textfile-database in the data folder
        with open("data/products.txt", "a") as file:
            file.write(prod_data + '\n')