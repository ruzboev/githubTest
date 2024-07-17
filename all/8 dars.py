
shopping_cart = ['apple', 'banana', 'orange', 'apple', 'apple', 'banana']


def handle_product_removal(cart):
    product_name = input("Enter product name: ").strip().lower()

    if product_name not in cart:
        print(f"{product_name.capitalize()} is not in the shopping cart.")
        return

    product_count = cart.count(product_name)

    if product_count == 1:
        cart.remove(product_name)
        print(f"{product_name.capitalize()} has been removed from the shopping cart.")
    elif product_count >= 2:
        while product_count > 1:
            response = input(
                f"{product_name.capitalize()} is in the cart {product_count} times. Do you want to delete 1 of them (yes to enable): ").strip().lower()
            if response == "yes":
                cart.remove(product_name)
                product_count -= 1
                print(f"One {product_name} has been removed. Remaining count: {product_count}")
            else:
                break

    # After handling, if the product was in the cart, show the current cart status
    if product_name in cart:
        print(f"Current shopping cart: {cart}")
    else:
        print(f"{product_name.capitalize()} has been completely removed from the shopping cart.")


# Execute the function
handle_product_removal(shopping_cart)