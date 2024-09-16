class Product:
    def __init__(self, name, category, description, price):
        self.name = name
        self.category = category
        self.description = description
        self.price = price

    def __str__(self):
        return f"{self.name} - {self.category}\n{self.description}\nPrice: ${self.price:.2f}\n"

def display_menu(products):
    print("Welcome to the Candy Store!")
    print("Please choose an item by number or letter:")
    for idx, product in enumerate(products):
        print(f"{idx + 1}. {product.name} - ${product.price:.2f}")

def payment_info():
    payment_type = input(
        "How would you like to pay?\nEnter 'Cash', 'Credit', 'Check', or 'Return' to return to menu: ")

    if payment_type.lower() == 'cash':
        cash_amount = float(input("Enter cash amount: $"))
        # Checks to see if amount paid is over or under the item price
        # if item_price < cash_amount:
        #     change = cash_amount - item_price
        #     print(f"Your change: ${change}")
        # elif item_price > cash_amount:
        #     print("Insufficient funds, please try again.")
        #     payment_type = input("Cash, Credit, or Check? ")
    elif payment_type.lower() == 'credit':
        card_number = int(input("Enter card number: "))
        expiration = int(input("Enter expiration date: "))
        cvv = int(input("Enter CVV: "))
    elif payment_type.lower() == 'check':
        check_number = int(input("Enter check number"))
    elif payment_type.lower() == 'return':
        main()

    redisplay = input("Return to menu? (y/n): ")
    if "y" in redisplay:
        main()
    elif "n" in redisplay:
        print("Subtotal: ")
        print("Payment info: ")
        if "cash" in payment_type:
            print(f"Cash: ${cash_amount}")
        elif "credit" in payment_type:
            print(f"Credit: {card_number}")
        elif "check" in payment_type:
            print(f"Check: {check_number}")

def main():
    # Create a list of Product instances
    products = [
        Product("Chocolate Bar", "Chocolate", "A delicious milk chocolate bar.", 1.99),
        Product("Gummy Bears", "Gummies", "Assorted fruit-flavored gummy bears.", 2.49),
        Product("Lollipop", "Suckers", "A colorful swirl lollipop.", 0.99),
        Product("Candy Corn", "Seasonal", "Classic Halloween candy corn.", 1.29),
        Product("Jelly Beans", "Jellies", "A mix of fruity jelly beans.", 2.79),
        Product("Caramel Chews", "Chews", "Chewy caramel candies.", 1.59),
        Product("Mint Drops", "Mints", "Refreshing mint candies.", 1.29),
        Product("Peanut Brittle", "Crunchy", "Crunchy peanut brittle.", 2.99),
        Product("Sour Worms", "Sour", "Sour and sweet gummy worms.", 2.69),
        Product("Sugar Sticks", "Hard Candy", "Sweet sugar sticks in various flavors.", 1.79),
        Product("Marshmallow Bites", "Marshmallows", "Chewy marshmallow bites.", 2.29),
        Product("Toffee", "Toffee", "Rich and buttery toffee pieces.", 2.89)
    ]

    # Display the menu
    display_menu(products)

    choice = input("\nEnter the number of the item you want to buy, or type 'exit' to quit: ").strip()

    if choice.lower() == 'exit':
        print("Thank you for visiting the Candy Store!")

    try:
        item_number = int(choice)
        selected_items = []
        if 1 <= item_number <= len(products):
            selected_product = products[item_number - 1]
            selected_items.append(selected_product)
            print(selected_items)
            print(f"\nYou have selected:\n{selected_product}")
            # --------BREAK---------
            payment_info()
            # --------BREAK---------
        else:
            print("Invalid number. Please select a number from the menu.")
    except ValueError:
        print("Invalid input. Please enter a number or 'exit'.")

if __name__ == "__main__":
    main()