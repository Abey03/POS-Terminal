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

    while True:
        choice = input("\nEnter the number of the item you want to buy, or type 'exit' to quit: ").strip()

        if choice.lower() == 'exit':
            print("Thank you for visiting the Candy Store!")

        try:
            item_number = int(choice)
            selected_items = []
            if 1 <= item_number <= len(products):
                selected_product = products[item_number - 1]
                selected_items.append(selected_product.name)
                selected_items.append(selected_product.price)
                print(f"\nYou have selected:\n{selected_product}")
                payment_type = input(
                    "How would you like to pay?\nEnter 'Cash', 'Credit', 'Check', or 'Return' to return to menu: ")

                # Sales tax and grand total variables
                sales_tax = selected_product.price * 0.06
                grand_total = round(sales_tax + selected_product.price, 2)

                if payment_type.lower() == 'cash':
                    cash_amount = float(input("Enter cash amount: $"))
                    # Checks to see if amount paid is over or under the item price to provide change
                    if grand_total < cash_amount:
                        change = cash_amount - grand_total
                        print(f"Your change: ${change}")
                    elif grand_total > cash_amount:
                        print("Insufficient funds, please try again.")
                        payment_type = input("Cash, Credit, or Check? ")
                elif payment_type.lower() == 'credit':
                    card_number = int(input("Enter card number: "))
                    expiration = int(input("Enter expiration date: "))
                    cvv = int(input("Enter CVV: "))
                elif payment_type.lower() == 'check':
                    check_number = int(input("Enter check number"))
                elif payment_type.lower() == 'return':
                    main()
                # Prompts the user to return to menu or checkout
                redisplay = input("Return to menu? (y/n): ")
                if "y" in redisplay:
                    continue
                elif "n" in redisplay:
                    print(
                        f"Items selected:\n{selected_items}\nSubtotal: ${selected_product.price}\n+ {round(sales_tax, 2)}(6% tax)\nGrand Total: {grand_total}\nPayment info")
                    if "cash" in payment_type:
                        print(f"Cash: ${cash_amount}\nChange: ${change}")
                    elif "credit" in payment_type:
                        print(f"Paid with card: {card_number}")
                    elif "check" in payment_type:
                        print(f"Paid with check: {check_number}")
            else:
                print("Invalid number. Please select a number from the menu.")
        except ValueError:
            print("Invalid input. Please enter a number or 'exit'.")

if __name__ == "__main__":
    main()