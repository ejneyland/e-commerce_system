class Product:
    
    # Product Constructor method
    def __init__(self, prod_id, prod_model, prod_category, prod_name, prod_current_price, prod_raw_price, prod_discount, prod_likes_count):
        self.prod_id = prod_id
        self.prod_model = prod_model
        self.prod_category = prod_category
        self.prod_name = prod_name
        self.prod_current_price = prod_current_price
        self.prod_raw_price = prod_raw_price
        self.prod_discount = prod_discount
        self.prod_likes_count = prod_likes_count

    # Product Str Object method
    def __str__(self):
        # defines a dictionary of Product attributes, key-value pairs
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
        # returns a string representation of the Product instance/object
        return str(prod_data)
    
# ------------------------------------------------------------