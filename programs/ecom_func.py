# Ecommerce using functions, dictionaries, lists, loops

# Step 0: main function
# Step 1: create products dictionary(container) in my_shop dictionary
# Step 2: create new product
# Step 3: update existing product
# Step 4: delete a product
# Step 5: show all products
# Step 6: show a single product

my_shop = {}

def create_products_container():
    # create a dictionary to store products
    # check if container exists
    if 'products' in my_shop:
        print("Products container already exists")
        return my_shop['products']
    else:
        my_shop['products'] = {}
        print('Products container created')
        return my_shop['products']


def create_product(products, product_name, product_price):
    # create a product
    # check if product exists
    if product_name in products:
        print("Product already exists")
        return products
    else:
        products[product_name] = product_price
        print("Product created")
        return products


def update_product(products, product_name, product_price):
    if product_name in products:
        products[product_name] = product_price
        print("Product has been updated")
        return products
    else:
        print("Product does not exist")
        return products


def delete_product(products, product_name):
    if not product_name in products:
        print("Product not found")
        return products

    del products[product_name]
    return products

def show_products(products):
    # pass
    if len(products) == 0:
        print("No products currently")
    else:
        for product_name, product_price in products.items():
            print(product_name, product_price)


def show_product(products, product_name):
    # pass
    if product_name in products:
        print(product_name, products[product_name])
    else:
        print("Product not found")


def main():
    # create products container
    products = create_products_container()

    while True:
        print('1. Create a product')
        print('2. Update a product')
        print('3. Delete a product')
        print('4. Show all products')
        print('5. Show a product')
        print('6. Exit')

        choice = input("Enter your choice: ")
        if choice == "1":
            product_name = input("Enter product name: ")
            product_price = input("Enter product price: ")
            products = create_product(products, product_name, product_price)
        elif choice == "2":
            product_name = input("Enter product name: ")
            product_price = input("Enter product price: ")
            products = update_product(products, product_name, product_price)
        elif choice == "3":
            # pass
            product_name = input("Enter product name: ")
            products = delete_product(products, product_name)
        elif choice == "4":
            # pass
            show_products(products)
        elif choice == "5":
            # pass
            product_name = input("Enter product name: ")
            show_product(products, product_name)
        elif choice == "6":
            break
        else:
            print("Invalid option")



main()