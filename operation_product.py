import random

class ProductOperation:
    
    existing_ids = set()

    @staticmethod
    def generate_prod_id():
        # starts with 'p_' followed by 5 digits
        # e.g. 'p_01234'
        while True:
            prod_id = 'p_' + ''.join(str(random.randint(0, 9)) for _ in range(5))
            # checks that the generated id is not already in the existing_ids
            # if prod_id already exists >> loop restarts >> new prod_id generated and checked
            if prod_id not in ProductOperation.existing_ids:
                # adds the uniquely generated id to the list of existing_ids
                ProductOperation.existing_ids.add(prod_id)
                # if id is unique >> id is returned
                return prod_id
            
    def save_to_file(product):
        # appends the string representation of a new Product instance to a textfile
        prod_data = str(product)
        # "a" option to 'append' to the prods textfile-database in the data folder
        with open("data/products.txt", "a") as file:
            file.write(prod_data + '\n')

    def extract_products_from_files():
        pass

    def get_product_list(page_number):
        pass # return tuple
    # including a list of products objects and the total number of pages. 
    # e.g. ([Product1,Product2,Product3,...Product10],p age_number, total_page)

    def delete_product(product_id):
        pass # return True/False

    def get_product_by_id(product_id):
        pass # a Product object or None if not found

    def generate_category_figure():
        pass

    def generate_discount_figure():
        pass

    def generate_likes_count_figure():
        pass

    def generate_discount_likes_count_figure():
        pass

    def delete_all_products():
        pass