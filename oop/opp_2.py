class Product:
    def __init__(self, name, product_id, price, stock):
        self.name = name
        self.product_id = product_id
        self.price = price
        self.stock = stock

    def update_stock(self, new_stock):
        self.stock = new_stock
        print("stock updated")


class Customer:
    def __init__(self, name, customer_id):
        self.name = name
        self.customer_id = customer_id
        self.orders = []


class Order:
    def __init__(self, order_id, customer):
        self.order_id = order_id
        self.customer = customer
        self.products = []
        self.total_amount = 0

    def add_product(self, product, quantity):
        # check product stock
        # update order total amount
        if product.stock >= quantity:
            product.update_stock(product.stock - quantity)
            self.total_amount += quantity * product.price
            print('product added')
        else:
            print(f'from {product.name} you can buy only {product.stock}')


class Store:
    def __init__(self):
        self.products = []
        self.customers = []
        self.total_sales = 0

    def add_product(self, product):
        self.products.append(product)
        print("product added")

    def add_customer(self, customer):
        self.customers.append(customer)

    def place_order(self, customer, order):
        # customer's orders update
        # total_sales update
        # print info
        customer.orders.append(order)
        self.total_sales += order.total_amount
        print('kassa updated')

    def display_products(self):
        # display products
        for product in self.products:
            print( f'{product.product_id}: {product.name.capitalize()} product, price {product.price} dan' )

    def update_product_stock(self, product_id, new_stock):
        ...
        # check if product is available in store
        # update product stock
        # give info about it



    def calculate_total_sales(self):
        # return total_sales
        return self.total_sales


store = Store()
product1 = Product("Laptop", "P001", 1500, 10)
product2 = Product("Phone", "P002", 800, 20)
customer1 = Customer("John", "C001")

store.add_product(product1)
store.add_product(product2)
store.add_customer(customer1)

order1 = Order("O001", customer1)
order1.add_product(product1, 5)
order1.add_product(product2, 7)
store.place_order(customer1, order1)

store.display_products()

store.update_product_stock("P001", 8)
print(f"Total sales: {store.calculate_total_sales()}")